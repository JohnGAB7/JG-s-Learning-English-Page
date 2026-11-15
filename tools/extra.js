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


/* Speak catalogue and first practice activities. Browser voice is generated,
   not a recorded speaker. Learner notes are saved only on explicit action. */
document.addEventListener("DOMContentLoaded",()=>{

  const siteSearch=document.querySelector("[data-site-search]");
  const siteResults=document.querySelector("[data-site-search-results]");
  if(siteSearch&&siteResults&&Array.isArray(window.SITE_SEARCH_INDEX)){
    siteSearch.addEventListener("input",()=>{
      const q=siteSearch.value.trim().toLocaleLowerCase();
      siteResults.replaceChildren();
      if(q.length<2)return;
      const matches=window.SITE_SEARCH_INDEX.filter(item=>
        (item.title+" "+item.description+" "+item.keywords).toLocaleLowerCase().includes(q)
      ).slice(0,10);
      if(!matches.length){
        const empty=document.createElement("p");
        empty.textContent=document.documentElement.lang==="fr"?"Aucun résultat.":"No results.";
        siteResults.append(empty);return;
      }
      matches.forEach(item=>{
        const link=document.createElement("a");
        link.href=item.url;
        const kind=document.createElement("small");
        kind.textContent=item.kind;
        const title=document.createElement("strong");
        title.textContent=item.title;
        const desc=document.createElement("span");
        desc.textContent=item.description;
        link.append(kind,title,desc);
        siteResults.append(link);
      });
    });
  }

  document.querySelectorAll("[data-speak-text]").forEach(button=>{
    button.addEventListener("click",()=>{
      if(!("speechSynthesis" in window)){button.textContent=document.documentElement.lang==="fr"?"La synthèse vocale n’est pas prise en charge par ce navigateur.":"Speech synthesis is not supported in this browser.";return;}
      window.speechSynthesis.cancel();
      const utterance=new SpeechSynthesisUtterance(button.dataset.speakText);
      utterance.lang="en-GB";
      utterance.rate=Math.max(.65,Math.min(1.15,Number(button.dataset.speakRate)||.88));
      window.speechSynthesis.speak(utterance);
    });
  });


  const studioCards=[...document.querySelectorAll('.studio-card[data-activity-id]')];
  if(studioCards.length){
    const progressKey='jg-studio-progress-v1',checklistKey='jg-studio-checklists-v1',vocabKey='jg-studio-vocab-drafts-v1';
    const readStore=key=>{try{const value=JSON.parse(localStorage.getItem(key)||'{}');return value&&typeof value==='object'&&!Array.isArray(value)?value:{};}catch(e){return {};}};
    const progress=readStore(progressKey),checklists=readStore(checklistKey),vocabDrafts=readStore(vocabKey);
    const storageNote=document.querySelector('[data-studio-storage-status]');
    let storageAvailable=true;try{localStorage.setItem('jg-studio-storage-check','1');localStorage.removeItem('jg-studio-storage-check');}catch(e){storageAvailable=false;}
    if(storageNote&&!storageAvailable)storageNote.textContent=document.documentElement.lang==='fr'?'Le stockage de ce navigateur est indisponible : la progression ne sera pas conservée après fermeture.':'Browser storage is unavailable; progress will not persist after closing this page.';
    const saveStore=(key,value)=>{try{localStorage.setItem(key,JSON.stringify(value));return true;}catch(e){if(storageNote)storageNote.textContent=document.documentElement.lang==='fr'?'Impossible d’enregistrer la progression dans ce navigateur.':'Could not save progress in this browser.';return false;}};
    const completedCount=()=>studioCards.filter(card=>progress[card.dataset.activityId]?.completed).length;
    const renderStudioProgress=()=>{
      studioCards.forEach(card=>{
        const record=progress[card.dataset.activityId];
        const done=!!record?.completed;
        const persisted=record?.persisted!==false;
        card.dataset.activityState=done?'completed':'incomplete';
        const status=card.querySelector('[data-activity-status]');
        if(status){
          status.textContent=done
            ?(persisted
              ?(document.documentElement.lang==='fr'?'Terminée sur cet appareil':'Completed on this device')
              :(document.documentElement.lang==='fr'?'Terminée pour cette session uniquement':'Completed for this session only'))
            :(document.documentElement.lang==='fr'?'Pas encore terminée':'Not completed yet');
          status.dataset.state=done?'completed':'incomplete';
        }
        const button=card.querySelector('[data-complete-activity]');
        if(button&&done){
          button.disabled=true;
          button.textContent=persisted
            ?(document.documentElement.lang==='fr'?'Activité terminée':'Activity completed')
            :(document.documentElement.lang==='fr'?'Terminée pour cette session':'Completed for this session');
        }
      });
      const count=completedCount(),label=document.querySelector('[data-studio-progress-count]'),bar=document.querySelector('[data-studio-progress-bar]');
      if(label)label.textContent=count+' / '+studioCards.length;
      if(bar)bar.value=count;
    };
    const completeStudioActivity=id=>{
      if(!id||progress[id]?.completed)return;
      const record={completed:true,completedAt:new Date().toISOString(),persisted:true};
      const next=Object.fromEntries(Object.entries(progress).map(([key,value])=>[
        key,value?.completed?{...value,persisted:true}:value
      ]));
      next[id]=record;
      const saved=saveStore(progressKey,next);
      if(saved)Object.assign(progress,next);
      else progress[id]={...record,persisted:false};
      renderStudioProgress();
    };
    document.addEventListener('studio:complete',event=>completeStudioActivity(event.detail?.id));
    const evaluateCompletion=card=>{
      const button=card.querySelector('[data-complete-activity]');
      if(!button||progress[card.dataset.activityId]?.completed)return;
      let ready=false;
      const rule=card.dataset.completionRule;
      if(rule==='self_check_all'||rule==='saved_draft_word_range_and_self_check'){
        const checklist=card.querySelector('[data-activity-checklist]');
        const checks=checklist?[...checklist.querySelectorAll('input[type="checkbox"]')]:[];
        ready=checks.length>0&&checks.every(input=>input.checked);
      }
      if(rule==='saved_draft_word_range_and_self_check'){
        const field=card.querySelector('[data-draft-field]'),counter=field&&document.querySelector('[data-word-count="'+field.id+'"]');
        const count=field?(field.value.trim().match(/\S+/g)||[]).length:0,min=counter?Number(counter.dataset.minWords)||0:0,max=counter?Number(counter.dataset.maxWords)||70:70;
        ready=ready&&!!field&&field.dataset.draftSaved==='true'&&count>=min&&count<=max;
      }
      if(rule==='learner_example_min_4_words_and_self_check'){
        const field=card.querySelector('[data-vocab-sentence]'),count=field?(field.value.trim().match(/\S+/g)||[]).length:0;
        const checklist=card.querySelector('[data-activity-checklist]');
        const checks=checklist?[...checklist.querySelectorAll('input[type="checkbox"]')]:[];
        ready=count>=4&&checks.length>0&&checks.every(input=>input.checked);
      }
      if(rule==='manual_review_confirmation')ready=true;
      button.disabled=!ready;
    };
    studioCards.forEach(card=>{
      const id=card.dataset.activityId,checklist=card.querySelector('[data-activity-checklist]');
      if(checklist){
        const checks=[...checklist.querySelectorAll('input[type="checkbox"]')],saved=Array.isArray(checklists[id])?checklists[id]:[];
        checks.forEach((input,index)=>{input.checked=saved[index]===true;input.addEventListener('change',()=>{checklists[id]=checks.map(item=>item.checked);saveStore(checklistKey,checklists);evaluateCompletion(card);});});
      }
      const vocab=card.querySelector('[data-vocab-sentence]');
      if(vocab){vocab.value=typeof vocabDrafts[id]==='string'?vocabDrafts[id]:'';vocab.addEventListener('input',()=>{vocabDrafts[id]=vocab.value;saveStore(vocabKey,vocabDrafts);evaluateCompletion(card);});}
      const draft=card.querySelector('[data-draft-field]');
      if(draft){draft.addEventListener('input',()=>{draft.dataset.draftSaved='false';evaluateCompletion(card);});draft.addEventListener('studio:draft-loaded',()=>evaluateCompletion(card));}
      const completeButton=card.querySelector('[data-complete-activity]');
      if(completeButton)completeButton.addEventListener('click',()=>{evaluateCompletion(card);if(!completeButton.disabled)completeStudioActivity(id);});
      evaluateCompletion(card);
    });
    renderStudioProgress();
  }

  document.querySelectorAll("[data-check-quiz]").forEach(button=>{
    button.addEventListener("click",()=>{
      const key=button.dataset.checkQuiz;
      const chosen=document.querySelector('input[name="'+key+'"]:checked');
      const feedback=document.querySelector('[data-quiz-feedback="'+key+'"]');
      if(!feedback)return;
      if(!chosen){
        feedback.textContent=document.documentElement.lang==="fr"?"Choisis une réponse avant de vérifier.":"Choose an answer before checking.";
        feedback.dataset.state="incomplete";
        return;
      }
      const correct=chosen.value===button.dataset.answer;
      feedback.textContent=correct
        ?(button.dataset.correctFeedback||(document.documentElement.lang==="fr"?"Bonne réponse. Tu peux maintenant révéler la transcription et approfondir.":"Correct. You can now reveal the transcript and explore further."))
        :(button.dataset.retryFeedback||(document.documentElement.lang==="fr"?"Pas tout à fait. Réessaie en te concentrant sur le sens général.":"Not quite. Try again and focus on the overall meaning."));
      feedback.dataset.state=correct?"correct":"retry";
      if(correct){const card=button.closest('.studio-card[data-activity-id]');if(card)document.dispatchEvent(new CustomEvent('studio:complete',{detail:{id:card.dataset.activityId}}));}
    });
  });

  document.querySelectorAll("[data-draft-field]").forEach(field=>{
    const key=field.dataset.draftField;
    const counter=document.querySelector('[data-word-count="'+key+'"]');
    const updateCount=()=>{
      const count=(field.value.trim().match(/\S+/g)||[]).length;
      if(counter){
        const min=Number(counter.dataset.minWords)||0;
        const max=Number(counter.dataset.maxWords)||70;
        counter.textContent=counter.dataset.label
          ?counter.dataset.label.replace("{count}",count)
          :(document.documentElement.lang==="fr"
            ?count+" / "+max+" mots · objectif : "+min+"–"+max
            :count+" / "+max+" words · target: "+min+"–"+max);
        counter.dataset.state=count===0?"empty":count<min?"below":count>max?"above":"in-range";
      }
    };
    try{const saved=localStorage.getItem("jg-writing-"+key);field.value=saved||"";field.dataset.draftSaved=saved!==null?"true":"false";}catch(e){field.dataset.draftSaved="false";}
    updateCount();
    field.dispatchEvent(new Event("studio:draft-loaded"));
    field.addEventListener("input",()=>{field.dataset.draftSaved="false";updateCount();});
  });

  const search=document.querySelector("[data-speaking-search]");
  const level=document.querySelector("[data-speaking-level]");
  const skill=document.querySelector("[data-speaking-skill]");
  const status=document.querySelector("[data-speaking-status]");
  if(search&&level&&skill&&status){
    const cards=[...document.querySelectorAll("[data-topic-card]")];
    const empty=document.querySelector("[data-speaking-empty]");
    const apply=()=>{
      let visible=0;
      cards.forEach(card=>{
        const q=search.value.trim().toLocaleLowerCase();
        const textMatch=!q||card.dataset.topicSearch.includes(q);
        const levelMatch=level.value==="all"||card.dataset.topicLevels.split(",").includes(level.value);
        const skillMatch=skill.value==="all"||card.dataset.topicSkills.split(",").includes(skill.value);
        const statusMatch=status.value==="all"||card.dataset.topicStatus===status.value;
        card.hidden=!(textMatch&&levelMatch&&skillMatch&&statusMatch);
        if(!card.hidden)visible++;
      });
      document.querySelectorAll("section[id^='universe-']").forEach(section=>{
        section.hidden=!section.querySelector("[data-topic-card]:not([hidden])");
      });
      if(empty)empty.hidden=visible>0;
    };
    search.addEventListener("input",apply);
    [level,skill,status].forEach(control=>control.addEventListener("change",apply));
    apply();
  }

  document.querySelectorAll("[data-save-response]").forEach(button=>{
    const key=button.dataset.saveResponse;
    const field=document.getElementById("response-"+key);
    const feedback=document.querySelector('[data-save-feedback="'+key+'"]');
    try{if(field)field.value=localStorage.getItem("jg-speaking-"+key)||"";}catch(e){}
    button.addEventListener("click",()=>{
      try{localStorage.setItem("jg-speaking-"+key,field?.value||"");if(feedback)feedback.textContent="Saved on this device.";}
      catch(e){if(feedback)feedback.textContent=document.documentElement.lang==="fr"?"Impossible d’enregistrer dans ce navigateur.":"Could not save in this browser.";}
    });
  });


  document.querySelectorAll("[data-complete-unit]").forEach(button=>{
    const key=button.dataset.completeUnit;
    const feedback=document.querySelector('[data-complete-feedback="'+key+'"]');
    const storageKey="jg-speaking-complete-"+key;
    const refresh=()=>{
      let done=false;try{done=localStorage.getItem(storageKey)==="1";}catch(e){}
      button.textContent=done?button.dataset.completedLabel:button.dataset.completeLabel;
      button.setAttribute("aria-pressed",String(done));
      if(feedback)feedback.textContent=done?"Progress saved on this device.":"";
    };
    refresh();
    button.addEventListener("click",()=>{
      let done=false;try{done=localStorage.getItem(storageKey)==="1";localStorage.setItem(storageKey,done?"0":"1");}catch(e){}
      refresh();
    });
  });

  document.querySelectorAll("[data-writing-save]").forEach(button=>{
    const key=button.dataset.writingSave,field=document.getElementById(key);
    const feedback=document.querySelector('[data-writing-feedback="'+key+'"]');
    try{if(field){const saved=localStorage.getItem("jg-writing-"+key);field.value=saved||"";field.dataset.draftSaved=saved!==null?"true":"false";}}catch(e){if(field)field.dataset.draftSaved="false";}
    button.addEventListener("click",()=>{
      try{localStorage.setItem("jg-writing-"+key,field?.value||"");if(field){field.dataset.draftSaved="true";field.dispatchEvent(new Event("studio:draft-loaded"));}if(feedback)feedback.textContent=document.documentElement.lang==="fr"?"Brouillon enregistré sur cet appareil.":"Draft saved on this device.";}
      catch(e){if(feedback)feedback.textContent=document.documentElement.lang==="fr"?"Impossible d’enregistrer dans ce navigateur.":"Could not save in this browser."; }
    });
  });
});


/* Browser-local learning overview. It reads existing stores; it creates no new profile. */
document.addEventListener("DOMContentLoaded",()=>{
  const dashboard=document.querySelector("[data-learning-dashboard]");
  if(!dashboard)return;
  const fr=document.documentElement.lang==="fr";
  const readObject=key=>{
    try{const value=JSON.parse(localStorage.getItem(key)||"{}");return value&&typeof value==="object"&&!Array.isArray(value)?value:{};}
    catch(e){return {};}
  };
  const setValue=(name,value)=>{
    const node=dashboard.querySelector('[data-learning-value="'+name+'"]');
    if(node)node.textContent=String(value);
  };
  const setProgress=(name,value,max)=>{
    const node=dashboard.querySelector('[data-learning-progress="'+name+'"]');
    if(node){node.max=Math.max(1,max);node.value=Math.min(value,max);}
  };
  const status=dashboard.parentElement.querySelector("[data-learning-storage-status]");
  try{
    const studioIds=JSON.parse(dashboard.dataset.studioIds||"[]");
    const speakingKeys=JSON.parse(dashboard.dataset.speakingKeys||"[]");
    const studio=readObject("jg-studio-progress-v1");
    const studioDone=studioIds.filter(id=>studio[id]?.completed).length;
    const speakingDone=speakingKeys.filter(key=>localStorage.getItem("jg-speaking-complete-"+key)==="1").length;
    const notes=speakingKeys.filter(key=>(localStorage.getItem("jg-speaking-"+key)||"").trim().length>0).length;
    const review=readObject("jg-review");
    const reviewCount=Object.keys(review).length;
    const priorityCount=Object.values(review).filter(value=>Number(value)>=5).length;
    const drafts=Object.keys(localStorage).filter(key=>key.startsWith("jg-writing-")&&(localStorage.getItem(key)||"").trim().length>0).length;
    setValue("studios",studioDone+" / "+studioIds.length);
    setValue("speaking",speakingDone+" / "+speakingKeys.length);
    setValue("review",reviewCount);
    setValue("review-priority",fr?priorityCount+" mot(s) à revoir en priorité":priorityCount+" word(s) marked for extra review");
    setValue("drafts",drafts);
    setValue("notes",notes);
    setProgress("studios",studioDone,studioIds.length);
    setProgress("speaking",speakingDone,speakingKeys.length);
    if(status)status.textContent=fr
      ?"Données lues sur cet appareil. Elles ne sont ni envoyées ni synchronisées."
      :"Progress read on this device. It is not uploaded or synchronised.";
  }catch(error){
    if(status)status.textContent=fr
      ?"Le stockage local est indisponible : cette vue ne peut pas lire ta progression."
      :"Local storage is unavailable, so this overview cannot read your progress.";
  }
});


/* Resume support: remember only the most recently opened lesson on this device. */
document.addEventListener("DOMContentLoaded",()=>{
  const lessonMatch=window.location.pathname.match(/\/(?:en\/)?lessons\/((?:a1|a2|b1|b2|c1)-\d{3})\/?$/i);
  if(lessonMatch){
    const heading=document.querySelector("main h1")||document.querySelector("h1");
    const record={
      id:lessonMatch[1].toLowerCase(),
      title:(heading?.textContent?.trim()||lessonMatch[1].toUpperCase()).slice(0,160),
      url:window.location.pathname,
      visitedAt:Date.now()
    };
    try{localStorage.setItem("jg-last-lesson-v1",JSON.stringify(record));}catch(error){}
  }

  const dashboard=document.querySelector("[data-learning-dashboard]");
  if(!dashboard)return;

  const fr=document.documentElement.lang==="fr";
  let record=null;
  try{
    const saved=JSON.parse(localStorage.getItem("jg-last-lesson-v1")||"null");
    if(saved&&typeof saved==="object"&&typeof saved.url==="string"){
      const target=new URL(saved.url,window.location.origin);
      const match=target.pathname.match(/\/(?:en\/)?lessons\/((?:a1|a2|b1|b2|c1)-\d{3})\/?$/i);
      if(target.origin===window.location.origin&&match){
        record={
          id:match[1].toLowerCase(),
          title:typeof saved.title==="string"&&saved.title.trim()?saved.title.trim().slice(0,160):match[1].toUpperCase(),
          url:target.pathname,
          visitedAt:Number.isFinite(saved.visitedAt)&&saved.visitedAt>0&&saved.visitedAt<=8640000000000000?saved.visitedAt:null
        };
      }
    }
  }catch(error){}

  const card=document.createElement("article");
  card.className="card learning-resume";
  card.setAttribute("aria-labelledby","learning-resume-title");
  const copy=document.createElement("div");
  copy.className="learning-resume-copy";
  const eyebrow=document.createElement("span");
  eyebrow.className="eyebrow";
  eyebrow.textContent=fr?"Reprendre":"Pick up where you left off";
  const heading=document.createElement("h2");
  heading.id="learning-resume-title";
  heading.textContent=record
    ?(fr?"Ta dernière leçon":"Your last lesson")
    :(fr?"Commencer le parcours":"Start your learning path");
  const description=document.createElement("p");
  description.textContent=record
    ?(fr?"Dernière leçon consultée : ":"Last lesson opened: ")+record.title
    :(fr?"Aucune leçon n’a encore été ouverte depuis cet appareil. Choisis un niveau et commence à ton rythme.":"You have not opened a lesson on this device yet. Choose a level and begin at your own pace.");
  copy.append(eyebrow,heading,description);

  if(record?.visitedAt){
    const time=document.createElement("time");
    time.className="learning-resume-time";
    time.dateTime=new Date(record.visitedAt).toISOString();
    time.textContent=(fr?"Consultée le ":"Opened on ")+new Intl.DateTimeFormat(fr?"fr-BE":"en-GB",{dateStyle:"medium"}).format(new Date(record.visitedAt));
    copy.append(time);
  }

  const link=document.createElement("a");
  link.className="button button-primary learning-resume-link";
  link.href=record?record.url:"../path/";
  link.textContent=record
    ?(fr?"Reprendre cette leçon →":"Continue this lesson →")
    :(fr?"Explorer le parcours →":"Explore the learning path →");
  card.append(copy,link);
  dashboard.insertAdjacentElement("afterend",card);
});
