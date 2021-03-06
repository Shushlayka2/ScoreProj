begin transaction;
drop table if exists criteria cascade;
drop table if exists institute cascade;
drop table if exists department cascade;
drop table if exists diploma  cascade;
drop table if exists professor cascade;
drop table if exists scope cascade;
drop trigger if exists user_signing on public.professor;
drop function if exists user_signing();
drop function if exists user_auth(text, text);
drop extension if exists pgcrypto;
commit;