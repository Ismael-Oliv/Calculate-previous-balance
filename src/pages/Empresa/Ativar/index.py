from PyQt5.QtWidgets import (
    QComboBox,
    QDockWidget,
    QLabel,
    QFrame,
    QPushButton
    )

from src.pages.Empresa.Ativar.services.index import AtivarServices

def AtivarFeature(Screen, ActiveCompany, ActiveCNPJ):

    def CloseEvent(Event):
        TXTEmpresa.setText('')


    def AtiveButtonClicked(TXTEmpresa, listButton):
        Empresa = TXTEmpresa.text()
        Cnpj = listButton.currentText()
        ActiveCompany.setText(Empresa)
        ActiveCNPJ.setText(Cnpj)

    def CancellButtonClicked():
        ActiveCompany.setText('')

    def listButtonChanges(TXTEmpresa, CNPJ):
        cnpj = CNPJ.currentText()
        companyName = AtivarServices.selectOne(cnpj)
        TXTEmpresa.setText(companyName[0][1])

    def listCompanyName(listButton):
        listOfCompany = AtivarServices.selectAll()
        arrListOfCompany = []

        for company in listOfCompany:
            arrListOfCompany.append(company[0])
            
        listButton.addItems(arrListOfCompany)


    Screen.setGeometry(5, 20, 590, 300)
    Screen.setFixedSize(590, 300)

    Frame = Screen.frame = QFrame(Screen)
    Frame.setGeometry(15,20,560,240)
    Frame.setFrameShape(QFrame.StyledPanel)

    LabelEmpresa = Screen.labelEmpresa = QLabel(Frame)
    LabelEmpresa.setGeometry(50,50,67,17)
    LabelEmpresa.setText('Empresa:')

    TXTEmpresa = Screen.txtEmpresa = QLabel(Frame)
    TXTEmpresa.setGeometry(130,50,321,17)
    TXTEmpresa.setStyleSheet("""
            background-color: rgb(186, 189, 182);
    """)

    LabelCNPJ = Screen.Labelcnpj = QLabel(Frame)
    LabelCNPJ.setGeometry(50,80,67,17)
    LabelCNPJ.setText('CNPJ:')

    # ==================================================
    # Lista de Empresas
    listButton = Screen.listbutton = QComboBox(Frame)
    listButton.setGeometry(130,80,191,25)
    listButton.currentTextChanged.connect(lambda:listButtonChanges(TXTEmpresa, listButton))

    listCompanyName(listButton)

    # ==================================================

    SaveButton = Screen.saveButton = QPushButton(Frame)
    SaveButton.setGeometry(140,150,101,31)
    SaveButton.setText('Ativar')
    SaveButton.clicked.connect(lambda: AtiveButtonClicked(TXTEmpresa, listButton))

    CancellButton = Screen.cancellbutton = QPushButton(Frame)
    CancellButton.setGeometry(300,150,101,31)
    CancellButton.setText('Cancelar')
    CancellButton.clicked.connect(CancellButtonClicked)


    Screen.closeEvent = CloseEvent
    Screen.show()
