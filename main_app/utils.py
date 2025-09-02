from django.utils import timezone

def generate_sequential_code(prefix: str, model, width: int = 4, extra: str | None = None) -> str:

    year = timezone.now().year
    parts = [prefix, str(year)]
    if extra:
        parts.insert(1, extra)  

    base = "-".join(parts) + "-"
    last = (model.objects.filter(code__startswith=base).order_by("-code").first())

    if last:
        try:
            last_num = int(last.code.split("-")[-1])
        except ValueError:
            last_num = 0
    else:
        last_num = 0

    return f"{base}{last_num + 1:0{width}d}"
