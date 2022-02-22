-- Table: public.Salas_Cine

-- DROP TABLE IF EXISTS public."Salas_Cine";

CREATE TABLE IF NOT EXISTS public."Salas_Cine"
(
    id integer NOT NULL DEFAULT nextval('"Salas_Cine_id_seq"'::regclass),
    provincia character varying COLLATE pg_catalog."default",
    cantidad_de_pantallas character varying COLLATE pg_catalog."default",
    cantidad_de_butacas character varying COLLATE pg_catalog."default",
    "cantidad_de_espacios_INCAA" character varying COLLATE pg_catalog."default",
    CONSTRAINT "Salas_Cine_pkey" PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Salas_Cine"
    OWNER to postgres;