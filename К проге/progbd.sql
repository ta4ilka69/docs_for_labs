create type WeaponType as ENUM(
    'HAMMER',
    'AXE',
    'PISTOL',
    'SHOTGUN',
    'BAT'
);

create type Mood as ENUM('SADNESS', 'RAGE', 'FRENZY');

create table humanbeing(
    id bigserial,
    name text,
    x numeric,
    y bigint,
    created_at TIME DEFAULT CURRENT_TIME,
    created_on DATE DEFAULT CURRENT_DATE,
    realHero boolean,
    hasToothpick boolean,
    impactSpeed numeric,
    soundtrackName text,
    weaponType WeaponType,
    mood Mood,
    carName text check (
        name is not null
        and name != ''
        and x > -257
        and realHero is not null
        and soundtrackName is not null
        and weaponType is not null
    )
);

insert into
    humanbeing (
        name,
        x,
        y,
        realHero,
        hasToothpick,
        impactSpeed,
        soundtrackName,
        weaponType,
        mood,
        carName
    )
values
    (
        'Gosling',
        23213.1231,
        123871248,
        true,
        false,
        219874.213,
        'phonk',
        'AXE',
        'RAGE',
        'Mustang'
    );