with
  vagas_perfil_filtered as (
    select
      vaga_id
    from
      public.vaga_perfil
    where
      perfil_id in (
        '2a53d96a-0229-42a9-8d15-278a2fdd87d4',
        '46773109-9bf3-4e7b-922a-2722e4183200'
      )
  ),
  vagas_filtered as (
    select
      tb1.*
    from
      public.vagas as tb1
      inner join vagas_perfil_filtered as tb2 on tb1.id = tb2.vaga_id
  )

select 
  titulo,
  descricao,
  empresa,
  localizacao
from
  vagas_filtered
