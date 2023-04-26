drop table humanbeing;
drop table users;
drop type WeaponType;
drop type Mood;

create type WeaponType as ENUM(
    'Rifle',
    'Knife',
    'Shotgun',
    'Machine gun'
);

create type Mood as ENUM('Longing', 'Gloom', 'Frenzy');

create table users(
    id bigserial primary key,
    login text unique,
    pass text,
    salt text
);
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
    carCool boolean,
    login text references users(login)
    check (
		id>0 and id is not null
        and name is not null
        and name != ''
        and x > -257
        and realHero is not null
        and soundtrackName is not null
        and weaponType is not null
    )
);
insert into users values (0,'GAF&f73Af#^fa','','');
select*from users;