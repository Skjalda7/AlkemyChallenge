-- Table: public.Turismo

-- DROP TABLE IF EXISTS public."Turismo";

CREATE TABLE IF NOT EXISTS public."Turismo"
(
    id integer NOT NULL DEFAULT nextval('"Turismo_id_seq"'::regclass),
    cod_localidad character varying COLLATE pg_catalog."default",
    id_provincia integer,
    id_departamento integer,
    categoria character varying COLLATE pg_catalog."default",
    provincia character varying COLLATE pg_catalog."default",
    localidad character varying COLLATE pg_catalog."default",
    nombre character varying COLLATE pg_catalog."default",
    domicilio character varying COLLATE pg_catalog."default",
    codigo_postal character varying COLLATE pg_catalog."default",
    numero_de_telefono character varying COLLATE pg_catalog."default",
    mail character varying COLLATE pg_catalog."default",
    web character varying COLLATE pg_catalog."default",
    CONSTRAINT "Turismo_pkey" PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Turismo"
    OWNER to postgres;