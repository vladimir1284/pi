{%- for indicator in indicators -%}
  {%- if indicator.type is in(["LowerTank", "UpperTank"]) %}
    {{indicator.id}} = new {{indicator.type}}("{{indicator.id}}", "{{indicator.label}}", {{indicator.min_level}}, {{indicator.capacity}})
  {%- endif %}  
  {%- if indicator.type is in(["Pump", "Light", "Door", "Pir", "Ldr"]) %}
    {{indicator.id}} = new {{indicator.type}}("{{indicator.id}}", "{{indicator.label}}")
  {%- endif %}
{%- endfor %}

indicators = [
{%- for indicator in indicators -%}
  {{indicator.id+","}}
{%- endfor -%}
]

indicators_dict = {
{%- for indicator in indicators -%}
  '{{indicator.id}}':{{indicator.id}},
{%- endfor -%}
}

room = "{{room}}"

