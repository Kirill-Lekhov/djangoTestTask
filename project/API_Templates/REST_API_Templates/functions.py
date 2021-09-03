def clear_separated_template(separated_template: list) -> list:
    return list(filter(lambda x: x, separated_template))


def normalize_separated_template(separated_template: list) -> list:
    normalized_template = []

    for template_part in separated_template:
        normalized_template.extend(template_part)

    return normalized_template


def find_variables(separated_templates: list) -> list:
    variables = []

    for separated_template in separated_templates[1:]:
        if len(separated_template) == 1:
            raise IndexError

        variables.append(separated_template[0])

    return variables


def split_template_by_variables(template: str) -> tuple:
    heat_was_added = False

    if template[:2] == "${":
        template = " " + template
        heat_was_added = True

    first_separated_template = clear_separated_template(template.split("${"))

    if heat_was_added:
        first_separated_template[0] = ""

    if len(first_separated_template) == 1:
        return [template], []

    second_separated_template = [template_part.split("}") for template_part in first_separated_template]
    variables = find_variables(second_separated_template)
    second_separated_template = normalize_separated_template(second_separated_template)
    second_separated_template = clear_separated_template(second_separated_template)

    return second_separated_template, variables


def find_variables_in_template(template: str) -> tuple:
    separated_template, variables = split_template_by_variables(template)

    return separated_template, variables


def template_variables_number(template: str) -> int:
    return len(find_variables_in_template(template)[1])


def put_variables_to_template(template: str, variables_and_values: dict) -> str:
    separated_template, variables = find_variables_in_template(template)
    completed_template = ""

    for template_part in separated_template:
        if template_part in variables:
            completed_template += variables_and_values[template_part]
            del variables[variables.index(template_part)]
            continue

        completed_template += template_part

    return completed_template
