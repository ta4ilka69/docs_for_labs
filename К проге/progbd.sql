drop table humanbeing;
drop type WeaponType;
drop type Mood;

create type WeaponType as ENUM(
    'RIFLE',
    'KNIFE',
    'SHOTGUN',
    'MACHINE_GUN'
);

create type Mood as ENUM('LONGING', 'GLOOM', 'FRENZY');

create table humanbeing(
    id bigserial,
    name text,
    x integer,
    y bigint,
    creationDate timestamp with time zone default CURRENT_TIMESTAMP,
    realHero boolean,
    hasToothpick boolean,
    impactSpeed bigint,
    soundtrackName text,
    weaponType WeaponType,
    mood Mood,
    carCool boolean check (
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
        carCool
    )
values
    (
        'Gosling',
        23213,
        123871248,
        true,
        false,
        219874,
        'phonk',
        'RIFLE',
        'GLOOM',
        true
    );
select*from humanbeing;