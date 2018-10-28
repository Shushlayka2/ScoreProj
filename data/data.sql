CREATE TABLE public.institute
(
    id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(40)
);
CREATE UNIQUE INDEX institute_id_uindex ON public.institute (id);

CREATE TABLE public.department
(
    id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(40),
    institute_id integer NOT NULL,
    CONSTRAINT institute_FK FOREIGN KEY (institute_id) REFERENCES public.institute (id)
);
CREATE UNIQUE INDEX department_id_uindex ON public.department (id);

CREATE TABLE public.professor
(
    full_name varchar(60) NOT NULL,
    id SERIAL PRIMARY KEY NOT NULL,
    is_expert boolean DEFAULT false  NOT NULL,
    department_id integer NOT NULL,
    CONSTRAINT department_FK FOREIGN KEY (department_id) REFERENCES public.department (id)
);
CREATE UNIQUE INDEX professor_id_uindex ON public.professor (id);

CREATE TABLE public.scope
(
    id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(30) NOT NULL
);
CREATE UNIQUE INDEX scope_id_uindex ON public.scope (id);

CREATE TABLE public.diploma
(
    id SERIAL PRIMARY KEY NOT NULL,
    thesis varchar(90) NOT NULL,
    description text NOT NULL,
    deadline date NOT NULL,
    team_work boolean DEFAULT false  NOT NULL,
    evaluation integer,
    professor_id INTEGER NOT NULL,
    scope_id INTEGER,
    CONSTRAINT professor_FK FOREIGN KEY (professor_id) REFERENCES public.professor (id),
    CONSTRAINT scope_FK FOREIGN KEY (scope_id) REFERENCES public.scope (id)
);
CREATE UNIQUE INDEX diploma_id_uindex ON public.diploma (id);

create table public.criteria
(
  id             serial  not null
    constraint criteria_pkey
    primary key,
  thesis_ev      integer not null,
  relevance_ev   integer not null,
  interest_ev    integer not null,
  feasibility_ev integer not null,
  expert_id      integer not null
    constraint expert_fk
    references professor,
  diploma_id     integer not null
    constraint diploma_fk
    references diploma
);
create unique index criteria_id_uindex
  on public.criteria (id);