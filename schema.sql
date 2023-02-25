drop table if exists Users;

create table Users (
    id integer primary key autoincrement,
    username varchar not null,
    email varchar not null,
    password text not null,
    role_id integer not null,
    critics_att varchar,
    foreign key (role_id) references Roles(id)
);

drop table if exists Roles;

create table Roles (
    id integer primary key autoincrement,
    name varchar
);

drop table if exists Texts;

create table Texts (
    id integer primary key autoincrement,
    title varchar not null,
    text_file varchar not null,
    release_date date not null,
    lang varchar not null,
    descr text not null,
    age_restr integer not null
);

drop table if exists Texts_Users;

create table Texts_Users (
    text_id integer not null,
    user_id integet not null,
    is_author boolean not null,
    foreign key (text_id) references Texts(id),
    foreign key (user_id) references Users(id)
);

drop table if exists Permissions;

create table Permissions (
    id integer primary key autoincrement,
    name varchar not null
);

drop table if exists Roles_Permissions;

create table Roles_Permissions (
    foreign key (permission_id) references Permissions(id),
    foreign key (role_id) references Role(id)
);

drop table if exists Tags;

create table Tags (
    id integer primary key autoincrement,
    name varchar not null
);

drop table if exists Texts_Tags;

create table Texts_Tags (
    foreign key (text_id) references Text(id),
    foreign key (tag_id) references Tag(id)
);

drop table if exists Fandoms;

create table Fandoms (
    id integer primary key autoincrement,
    name varchar not null
);

create table Texts_Fandoms (
    foreign key (text_id) references Text(id),
    foreign key (fandom_id) references Fandom(id)
);

