-- Table: public.Registros

-- DROP TABLE IF EXISTS public."Registros";

CREATE TABLE IF NOT EXISTS public."Registros"
(
    id integer NOT NULL DEFAULT nextval('"Registros_id_seq"'::regclass),
    categoria character varying COLLATE pg_catalog."default",
    fuente character varying COLLATE pg_catalog."default",
    provincia_y_categoria character varying COLLATE pg_catalog."default",
    CONSTRAINT "Registros_pkey" PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Registros"
    OWNER to postgres;