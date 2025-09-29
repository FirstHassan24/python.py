# 001-lesson-django-request-to-response

Quest: See how Django’s parts click together from a browser request to the final HTML response — using Monster Hunter and FGO flavor. 🐲✨

---

## Big Picture (Request -> Response)

1) Browser makes a request (URL) → "I want /hunts/ or /servants/"
2) `urls.py` routes the request → "Send this to the right hunter (view)."
3) `views.py` (the controller/brain) → "Fetch data, apply logic, choose a template."
4) `models.py` (your data schema) → "Define Monsters, Quests, Servants, Classes."
5) ORM query → "Get monsters/servants from the database."
6) Template (`.html`) → "Render a page with that data."
7) Response → "Return HTML to the browser."

Boss mechanic to remember: Views orchestrate; Models store; Templates display; URLs connect. Admin is a bonus armory for managing data.

---

## How the Pieces Fit (with examples)

- URL: `/hunts/` → shows a list of Monster Hunter quests.
- URLconf (`urls.py`): Pattern `path('hunts/', hunts_list)` sends to the `hunts_list` view.
- View (`views.py`): `hunts_list` uses the ORM to pull `Quest` objects from the DB.
- Model (`models.py`): `Quest(name, rank, target_monster, reward_zenny)` defines the data.
- Template (`hunts_list.html`): Loops over quests and renders them nicely.
- Response: The rendered HTML goes back to the browser.

FGO mirror example:
- URL: `/servants/` → list of Servants.
- Model: `Servant(name, class_type, rarity, np_name)`.
- View: Fetch all 5★ Sabers.
- Template: Show cards with name, class icon, and NP.

---

## Minimal Glossary

- Project vs App: A project is your entire kingdom; an app is a guild hall (focused feature). Projects often have multiple apps.
- `settings.py`: World config (DB, installed apps, templates, static).
- Migrations: Evolution stones for your DB schema. Create → migrate.
- Admin: Free forge to create/edit data fast.
- Static files: Images/CSS/JS. Media files: user-uploaded loot.

---

## Typical Flow You’ll Build

- Define Models → Make Migrations → Register in Admin → Create Data
- Add URL patterns → Write Views → Query via ORM → Render Templates
- Style, iterate, and add forms for create/update/delete (CRUD)

---

## Mental Model (TL;DR)

URL → View → (Model/ORM) → Template → Response

Think of Views as the field team lead, Models as the database bestiary, Templates as the quest board UI, and URLs as the dispatcher.

---

## XP Check

Rate your grasp of this map (1 = confused, 2 = partial, 3 = got it). Then we’ll build a tiny "Quest Log" app next. 🗒️⚔️
