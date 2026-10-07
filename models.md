# SkillMatch JSON data shapes

All files live in the project’s `data/` directory and are read or written through
`data_store.py`. Each top-level JSON object is keyed by the record identifier.
The examples below show the complete record shapes used by the shared foundation.

## `users.json`

The key is the user's username. `role` is either `Organizer` or
`Student Volunteer`. `dept` is `null` for organizers and a department name for
student volunteers. Skill ratings are non-negative integers; the foundation does
not impose an upper limit.

```json
{
  "samira": {
    "password_hash": "<stored password hash>",
    "role": "Student Volunteer",
    "name": "Samira Patel",
    "dept": "Environmental Science",
    "skills": {
      "Photography": 4,
      "Event planning": 3
    }
  }
}
```

The attached command-line prototype stores raw passwords in a `password` field.
Do not carry that into new features; use a password hash if password-based
accounts are implemented.

## `events.json`

The key is the event ID. `organizer` refers to a username in `users.json`.
`required_skills` maps skill names to minimum non-negative ratings, and
`slots_needed` is a positive integer.

```json
{
  "campus-garden-day": {
    "name": "Campus Garden Day",
    "description": "Help prepare the community garden for spring.",
    "organizer": "lee",
    "required_skills": {
      "Gardening": 2
    },
    "slots_needed": 8,
    "status": "open"
  }
}
```

Event status is `open` or `completed`.

## `applications.json`

The first key is the event ID; the nested key is the applicant's username.
`role` is `null` until an organizer accepts the application. `hours` is
non-negative and `notes` is a string.

```json
{
  "campus-garden-day": {
    "samira": {
      "status": "pending",
      "role": null,
      "hours": 0,
      "notes": ""
    }
  }
}
```

Application status is `pending`, `accepted`, or `rejected`.
