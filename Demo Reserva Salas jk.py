import sys

from PyQt5.QtWidgets import QApplication, QDialog
from IntResSalas import Ui_HotelSistemaReservas

class AplicacionHotel(QDialog):

    def __init__(self):
        super().__init__()

        self.inicializarGui()

    def inicializarGui(self):
        self.ui = Ui_HotelSistemaReservas()
        self.ui.setupUi(self)

        self.ui.btn_calcular.clicked.connect(self.mostrar_resumen)

        self.show()

    def mostrar_resumen(self):
        fecha = self.ui.cal_fecha_reserva.selectedDate()
        fecha_texto = str(fecha.toPyDate())
        dias = self.ui.sbx_cantidad_dias.value()
        indice = self.ui.cbx_tipo_habitacion.currentIndex()
        tipo_habitacion = self.ui.cbx_tipo_habitacion.itemText(indice)

        resumen = f"""
        Fecha: {fecha_texto}
        Horas: {dias}
        Tipo de Sala: {tipo_habitacion}
        A Cargo de Juan Caros 
        """

        self.ui.txt_resumen_seleccion.setText(resumen)

        if tipo_habitacion == "Reunion chica":
            costo = 10
        elif tipo_habitacion == "Reunion grande":
            costo = 20
        elif tipo_habitacion == "Multimedia":
            costo = 50
        else:
            costo = 100

        self.ui.txt_costo.setText(f'{costo:,}')

def main():
    app = QApplication(sys.argv)
    dialogo = AplicacionHotel()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()