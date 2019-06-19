CREATE SEQUENCE public.s_idsessao
    INCREMENT 1
    START 57
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;


    CREATE TABLE public.pessoa
(
    id integer NOT NULL,
    nome text COLLATE pg_catalog."default" NOT NULL,
    senha text COLLATE pg_catalog."default" NOT NULL,
    email text COLLATE pg_catalog."default",
    endereco text COLLATE pg_catalog."default",
    cidade text COLLATE pg_catalog."default",
    bairro text COLLATE pg_catalog."default",
    cep integer,
    CONSTRAINT pessoas_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;



    CREATE TABLE public.sessao
(
    id integer,
    usuario integer,
    mac_adress numeric
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;
