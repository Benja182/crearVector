class Eventos:
    def __init__(self, codigo, titulo, descripcion, costo, tipo, segmento):
        self.codigo = codigo
        self.titulo = titulo
        self.descrip = descripcion
        self.costo = float(costo)
        self.tipo = tipo
        self.segmento = segmento


def to_string(reg):
    linea = '{:<15}\t{:<15}\t{:<50}\t{:<30}\t{:<15}\t{:<15}\n'
    linea = linea.format(reg.codigo, reg.titulo, reg.descrip, reg.costo, reg.tipo, reg.segmento)
    return linea
