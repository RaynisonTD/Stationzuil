PGDMP                      {            Stationzuil    16.0    16.0     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16575    Stationzuil    DATABASE     �   CREATE DATABASE "Stationzuil" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE "Stationzuil";
                postgres    false            �            1259    24777 	   berichten    TABLE     '  CREATE TABLE public.berichten (
    naam character varying,
    leeftijd integer,
    bericht character varying,
    station character varying,
    datum timestamp without time zone,
    goedgekeurd character varying,
    gekeurd_door character varying,
    moderator_email character varying
);
    DROP TABLE public.berichten;
       public         heap    postgres    false            �          0    24777 	   berichten 
   TABLE DATA           x   COPY public.berichten (naam, leeftijd, bericht, station, datum, goedgekeurd, gekeurd_door, moderator_email) FROM stdin;
    public          postgres    false    215   #       �   �   x�Uο� ��x��@�4�L�87�����?	���B��%���;cp�7pt)�8�Ny�2�RѰI��#\^�H�wEi�d�LJu�=G�\��T�L�*���v���6��I�挥��Q
W��c�ǅYG�!*����%���H5[     