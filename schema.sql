drop table if exists Users;

create table Users (
    id integer primary key autoincrement,
    username varchar(50) not null,
    email varchar(50) not null,
    password text not null,
    role_id integer not null,
    critics_att varchar(255),
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
    title varchar(255) not null,
    text_file varchar(255) not null,
    release_date date not null,
    lang varchar(50) not null,
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
