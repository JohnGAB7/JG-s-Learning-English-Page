# Privacy notice — JG's Learning English

> Draft for legal review. Do not publish until controller identity/contact details, retention and final processor/transfer information are confirmed.

## Français

JG's Learning English permet d'apprendre sans compte obligatoire. Si l'apprenant crée volontairement un compte, les données traitées sont limitées à son adresse e-mail (authentification) et à sa progression : identifiants stables de contenus, état (« commencé » ou « terminé ») et date de mise à jour. La finalité est exclusivement de conserver et synchroniser cette progression entre appareils. Les brouillons d'écriture restent locaux par défaut.

**Responsable du traitement :** John [nom légal complet et coordonnées à confirmer avant publication].

**Hébergement prévu :** Union européenne, région Supabase EU (Francfort), à vérifier dans la configuration réelle avant toute collecte.

**Sous-traitant :** Supabase, Inc. pour l'authentification et la base de données, sous réserve de vérifier l'entité contractante, les sous-traitants ultérieurs et les conditions applicables.

**Conservation :** durée à définir et publier avant l'ouverture des comptes. La suppression du compte entraîne la suppression en cascade des lignes de progression.

**Demandes relatives aux données et suppression :** [adresse de contact à renseigner]. La suppression du compte devra passer par un mécanisme serveur sécurisé, jamais par une clé service-role exposée au navigateur.

**Limite de réinitialisation V1 :** aucune tombstone n'est prévue. Une ligne supprimée peut être recréée par un autre appareil qui détient encore cette progression. Cette limite doit être expliquée dans l'interface ou résolue ultérieurement avec un mécanisme reset_at/tombstone.

## English

JG's Learning English supports guest learning without a mandatory account. If a learner voluntarily creates an account, processing is limited to their email address (authentication) and learning progress: stable content IDs, status ("started" or "completed"), and update timestamp. The sole purpose is to retain and synchronise progress across devices. Writing drafts remain local by default.

**Data controller:** John [full legal name and contact details to be confirmed before publication].

**Planned hosting:** European Union, Supabase EU (Frankfurt) region, to be verified in the actual project configuration before collecting data.

**Processor:** Supabase, Inc. for authentication and database services, subject to verification of the contracting entity, subprocessors and applicable terms.

**Retention:** period to be defined and published before accounts are opened. Account deletion cascades to associated progress rows.

**Data requests and account deletion:** [contact address to be completed]. Account deletion must use a secure server-side mechanism; a service-role key must never be exposed in the browser.

**V1 reset limitation:** there are no progress tombstones. A deleted row may be recreated by another device that still holds the progress. This must be explained in the reset UI or addressed later with reset_at/tombstones.

## Release checklist

- [ ] Confirm John's legal controller identity and public contact details.
- [ ] Define and publish a proportionate retention period.
- [ ] Verify actual Supabase EU (Frankfurt) region.
- [ ] Verify Supabase contracting entity, DPA, subprocessors and transfer terms.
- [ ] Implement account deletion through a secure server-side function/RPC.
- [ ] Explain reset semantics or implement tombstones.
- [ ] Complete legal review and publish both language versions before enabling accounts.
