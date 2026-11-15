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

/* ---- Thème clair/sombre JG's Learning English ---------------------------
 * Le thème initial est posé AVANT la première peinture par un script inline
 * du <head> qui lit `localStorage.getItem("ab-theme")`. Ici on se contente
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
    try{localStorage.setItem("ab-theme",t);}catch(e){}
    const metaTheme=document.querySelector('meta[name="theme-color"]');
    if(metaTheme)metaTheme.setAttribute("content",t==="dark"?"#0f1619":"#f8f6ef");
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

/* ---- JG's Learning English: print, programme, review cards, news tabs ---- */
document.addEventListener("DOMContentLoaded",()=>{
  const search=document.querySelector("[data-search]");
  search?.addEventListener("input",()=>{if(search.value.trim())document.querySelectorAll(".soon-list").forEach(d=>d.open=true);});
  document.querySelectorAll("[data-print]").forEach(b=>b.addEventListener("click",()=>{document.querySelectorAll("details.answer").forEach(d=>d.open=true);window.print();}));

  const card=document.querySelector("[data-flashcard]");
  if(card&&window.REVIEW_CARDS){
    const all=window.REVIEW_CARDS,$=s=>document.querySelector(s);
    const lvl=$("[data-review-level]"),dir=$("[data-review-dir]");
    let w={};try{w=JSON.parse(localStorage.getItem("jg-review")||"{}");}catch(e){}
    const save=()=>{try{localStorage.setItem("jg-review",JSON.stringify(w));}catch(e){}};
    let cur=null,known=0,seen=0;
    const pick=()=>{const pool=all.filter(c=>lvl.value==="all"||c.lvl===lvl.value);let tot=0;const ws=pool.map(c=>{const x=w[c.en]??3;tot+=x;return x;});let r=Math.random()*tot;for(let i=0;i<pool.length;i++){r-=ws[i];if(r<=0)return pool[i];}return pool[pool.length-1];};
    const show=()=>{cur=pick();const en=dir.value==="en";$("[data-fc-meta]").textContent=`${cur.lvl} · lesson ${cur.n}`;$("[data-fc-front]").textContent=en?cur.en:cur.def;
      const back=$("[data-fc-back]");back.hidden=true;back.innerHTML="";const b=document.createElement("b");b.textContent=en?cur.def:cur.en;const p=document.createElement("p");p.lang="en";p.textContent=cur.ex;const a=document.createElement("a");a.href=cur.url;a.textContent=document.documentElement.lang==="fr"?"Retour à la leçon →":"Back to the lesson →";back.append(b,p,a);};
    const flip=()=>{const b=$("[data-fc-back]");b.hidden=!b.hidden;};
    const mark=ok=>{seen++;if(ok)known++;w[cur.en]=Math.max(1,Math.min(9,(w[cur.en]??3)+(ok?-1:2)));save();$("[data-fc-score]").textContent=document.documentElement.lang==="fr"?`Cette séance : ${known} sur ${seen} connus.`:`This session: ${known} known out of ${seen}.`;show();};
    card.addEventListener("click",flip);card.addEventListener("keydown",e=>{if(e.key==="Enter"||e.key===" "){e.preventDefault();flip();}});
    $("[data-fc-flip]").addEventListener("click",flip);$("[data-fc-know]").addEventListener("click",()=>mark(true));$("[data-fc-again]").addEventListener("click",()=>mark(false));
    lvl.addEventListener("change",show);dir.addEventListener("change",show);show();
  }

  const tabs=[...document.querySelectorAll("[data-tab]")];
  if(tabs.length){
    const news=[...document.querySelectorAll("[data-pays]")],empty=document.querySelector("[data-news-empty]");
    const select=k=>{tabs.forEach(t=>t.setAttribute("aria-selected",String(t.dataset.tab===k)));let n=0;news.forEach(x=>{const ok=k==="all"||x.dataset.pays===k;x.hidden=!ok;if(ok)n++;});if(empty)empty.hidden=n>0;try{localStorage.setItem("jg-pays",k);}catch(e){}};
    tabs.forEach(t=>t.addEventListener("click",()=>select(t.dataset.tab)));
    let s="all";try{s=localStorage.getItem("jg-pays")||"all";}catch(e){}
    select(tabs.some(t=>t.dataset.tab===s)?s:"all");
  }
});
