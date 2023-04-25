drop table humanbeing;
drop type WeaponType;
drop type Mood;

create type WeaponType as ENUM(
    'Rifle',
    'Knife',
    'Shotgun',
    'Machine gun'
);

create type Mood as ENUM('Longing', 'Gloom', 'Frenzy');

create table humanbeing(
    id bigserial primary key,
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
		id>0 and id is not null
        and name is not null
        and name != ''
        and x > -257
        and realHero is not null
        and soundtrackName is not null
        and weaponType is not null
    )
);

insert into
    humanbeing (
		id,
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
		default,
        'Gosling',
        2323,
        123871248,
        true,
        false,
        219874,
        'phonk',
        'Rifle',
        'Gloom',
        true
    );
insert into
    humanbeing (
		id,
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
		12,
        'Hz',
        2323,
        123848,
        false,
        true,
        4,
        'kizaru',
        'Shotgun',
        'Frenzy',
        true
    );
insert into
    humanbeing (
		id,
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
		8,
        'Hz',
        2323,
        123848,
        false,
        true,
        4,
        'kizaru',
        'Shotgun',
        'Frenzy',
        true
    );
select*from humanbeing;