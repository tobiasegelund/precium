import attrs


@attrs.define
class Item:
    no: int = attrs.field(validator=attrs.validators.instance_of(int))
