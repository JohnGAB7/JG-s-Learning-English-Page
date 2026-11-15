document.addEventListener("DOMContentLoaded",()=>{
  const toggle=document.querySelector(".menu-toggle");
  const nav=document.querySelector(".nav-links");
  if(toggle&&nav){
    const isFrench=document.documentElement.lang.toLowerCase().startsWith("fr");
    const openLabel=isFrench?"Ouvrir le menu":"Open menu";
    const closeLabel=isFrench?"Fermer le menu":"Close menu";
    const setOpen=(open,returnFocus=false)=>{
      nav.classList.toggle("is-open",open);
      toggle.setAttribute("aria-expanded",String(open));
      toggle.setAttribute("aria-label",open?closeLabel:openLabel);
      if(!open&&returnFocus)toggle.focus();
    };
    toggle.addEventListener("click",()=>setOpen(!nav.classList.contains("is-open")));
    document.addEventListener("keydown",event=>{
      if(event.key==="Escape"&&nav.classList.contains("is-open"))setOpen(false,true);
    });
    document.addEventListener("click",event=>{
      if(nav.classList.contains("is-open")&&!nav.contains(event.target)&&!toggle.contains(event.target))setOpen(false);
    });
    nav.addEventListener("click",event=>{
      if(event.target.closest("a"))setOpen(false);
    });
    window.addEventListener("resize",()=>{
      if(window.matchMedia("(min-width: 851px)").matches)setOpen(false);
    });
  }
  const search=document.querySelector("[data-search]");
  const filter=document.querySelector("[data-filter]");
  const cards=[...document.querySelectorAll("[data-lesson]")];
  const empty=document.querySelector("[data-empty]");
  const sections=[...document.querySelectorAll("[data-module-section]")];
  const isFrenchLib=document.documentElement.lang.toLowerCase().startsWith("fr");
  const lessonWord=isFrenchLib?"leçon":"lesson";
  const lessonsWord=isFrenchLib?"leçons":"lessons";
  const apply=()=>{
    const q=(search?.value||"").trim().toLocaleLowerCase();
    const f=filter?.value||"all";
    let visible=0;
    cards.forEach(card=>{
      const text=(card.textContent+" "+(card.dataset.keywords||"")).toLocaleLowerCase();
      const category=card.dataset.category||"all";
      card.hidden=!(text.includes(q)&&(f==="all"||f===category));
      if(!card.hidden)visible++;
    });
    sections.forEach(sec=>{
      const kept=[...sec.querySelectorAll("[data-lesson]")].filter(c=>!c.hidden).length;
      sec.hidden=kept===0;
      const counter=sec.querySelector("[data-visible-count]");
      if(counter)counter.textContent=kept+" "+(kept===1?lessonWord:lessonsWord);
    });
    if(empty)empty.hidden=visible!==0;
  };
  search?.addEventListener("input",apply);
  filter?.addEventListener("change",apply);
  apply();
});

/* ---- JG’s Learning English: light/dark theme ------------------------------
 * Le thème initial est posé AVANT la première peinture par un script inline
 * du <head> qui lit `localStorage.getItem("jg-learning-theme")||localStorage.getItem("ab-theme")`. Ici on se contente
 * de câbler la bascule : clic ↔ data-theme ↔ localStorage.
 */
document.addEventListener("DOMContentLoaded",()=>{
  const btns=document.querySelectorAll("[data-theme-toggle]");
  if(!btns.length)return;
  const html=document.documentElement;
  const getCurrent=()=>{
    const explicit=html.getAttribute("data-theme");
    if(explicit==="dark"||explicit==="light")return explicit;
    return matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light";
  };
  const apply=(t)=>{
    html.setAttribute("data-theme",t);
    try{localStorage.setItem("jg-learning-theme",t);}catch(e){}
    const metaTheme=document.querySelector('meta[name="theme-color"]');
    if(metaTheme)metaTheme.setAttribute("content",t==="dark"?"#0D1C1A":"#F7F5EF");
  };
  btns.forEach(b=>{
    b.addEventListener("click",()=>apply(getCurrent()==="dark"?"light":"dark"));
  });
});

/* ---- Table des matières sticky sur les pages leçons ---------------------
 * Alimentée par les <h2> de .lesson-content. Indique la section active
 * pendant le défilement. Pas de polyfill : IntersectionObserver suffit.
 */
document.addEventListener("DOMContentLoaded",()=>{
  const nav=document.querySelector("[data-lesson-toc]");
  const content=document.querySelector(".lesson-content");
  if(!nav||!content)return;
  const headings=content.querySelectorAll("h2");
  if(!headings.length){nav.remove();return;}
  const list=document.createElement("ol");
  list.className="lesson-toc-list";
  const links=new Map();
  headings.forEach((h,i)=>{
    if(!h.id)h.id="s-"+(i+1)+"-"+(h.textContent||"").toLowerCase().replace(/[^\w]+/g,"-").slice(0,40);
    const li=document.createElement("li");
    const a=document.createElement("a");
    a.href="#"+h.id;
    a.textContent=h.textContent;
    li.appendChild(a);
    list.appendChild(li);
    links.set(h.id,a);
  });
  nav.appendChild(list);
  const io=new IntersectionObserver((entries)=>{
    entries.forEach(e=>{
      const a=links.get(e.target.id);
      if(!a)return;
      if(e.isIntersecting)a.classList.add("is-active");
      else a.classList.remove("is-active");
    });
  },{rootMargin:"-30% 0px -60% 0px",threshold:0});
  headings.forEach(h=>io.observe(h));
});
