from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDockWidget
from src.pages.Empresa.Ativar.index import AtivarFeature
from src.pages.Empresa.Cadastrar.index import CadastrarFeature
from src.pages.Empresa.Editar.index import EditarFeature
from src.pages.Importar.xml.index import XMLFeature
from src.pages.Importar.RegistroC170.index import RegistroC170Feature
from src.pages.Correcoes.Cest.index import CorrigirCestFeature
from src.pages.Correcoes.Registro0200.index import Corrigir0220Feature
from src.pages.Analises.XMLemSPED.index import XMLInSPEDFeature
from src.pages.Uteis.Calc_ICMS_ressar.index import CalcICMSRessarFeature
from src.pages.Exportar.Saldo_Inicial.index import SaldoInicialFeature
from src.pages.Uteis.NFs_Transf_ST.index import FindXMlWithoutStFeature
from src.pages.Importar.cadastro_produtos.index import ImportarCadastroProdutosFeature
from src.pages.Importar.RegistroH010.index import RegistroH010Feature
from src.pages.Importar.Codigo_Relacionamento.index import ImportarCodigoRelacionamentoFeature

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        # ============================================================================
        # Header

        MainWindow.setObjectName("")
        MainWindow.setMinimumSize(603, 534)
        MainWindow.setMaximumSize(603, 534)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        # =================Sessao de Empresa Ativa====================
        self.LabelCnpjCompany = QtWidgets.QLabel(self.centralwidget)
        self.LabelCnpjCompany.setGeometry(QtCore.QRect(240, 0, 90, 21))
        self.LabelCnpjCompany.setText("CNPJ: ")

        self.ActiveCNPJ = QtWidgets.QLabel(self.centralwidget)
        self.ActiveCNPJ.setGeometry(QtCore.QRect(280, 0, 111, 21))
        self.ActiveCNPJ.setText("")
        self.ActiveCNPJ.setObjectName("ActiveCNPJ")

        self.TxtCnpjCompany = QtWidgets.QLabel(self.centralwidget)
        self.TxtCnpjCompany.setGeometry(QtCore.QRect(420, 0, 90, 21))
        self.TxtCnpjCompany.setText("Empresa: ")

        self.ActiveCompany = QtWidgets.QLabel(self.centralwidget)
        self.ActiveCompany.setGeometry(QtCore.QRect(486, 0, 111, 21))
        self.ActiveCompany.setText("")
        self.ActiveCompany.setObjectName("ActiveCompany")
        # ====================================================================================


        # ====================================================================================
        #                   Criar Menu
        # ====================================================================================

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 603, 22))
        self.menubar.setObjectName("menubar")

        self.menuEmpresa = QtWidgets.QMenu(self.menubar)
        self.menuEmpresa.setObjectName("menuEmpresa")

        self.menuImportar = QtWidgets.QMenu(self.menubar)
        self.menuImportar.setObjectName("menuImportar")

        self.menuExportar = QtWidgets.QMenu(self.menubar)
        self.menuExportar.setObjectName("menuExportar")

        self.menuAnalise = QtWidgets.QMenu(self.menubar)
        self.menuAnalise.setObjectName('menuAnalise')

        self.menuCorrecoes = QtWidgets.QMenu(self.menubar)
        self.menuCorrecoes.setObjectName("menuCorrecoes")

        self.menuUteis = QtWidgets.QMenu(self.menubar)
        self.menuUteis.setObjectName('menuUteis')

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # ====================================================================================


        # ====================================================================================
        # Criação das telas
        # ====================================================================================
        self.AlertScreen = QDockWidget(self.centralwidget)
        self.AlertScreen.hide()
        # ==================Ativar Empresa====================================================
        self.AtivarEmpresaScreen = QDockWidget(self.centralwidget)
        self.AtivarEmpresaScreen.hide()

        # ==================Cadastrar Empresa=================================================
        self.CadastrarEmpresaScreen = QDockWidget(self.centralwidget)
        self.CadastrarEmpresaScreen.hide()

        # ==================Editar Empresa====================================================
        self.EditarEmpresaScreen = QDockWidget(self.centralwidget)
        self.EditarEmpresaScreen.hide()
        # ====================================================================================

        # ==================Importar XML====================================================
        self.ImportarXMLScreen = QDockWidget(self.centralwidget)
        self.ImportarXMLScreen.hide()
        # ====================================================================================

        # ==================Importar Registro C170============================================
        self.ImportarC170Screen = QDockWidget(self.centralwidget)
        self.ImportarC170Screen.hide()
        # ====================================================================================

        # ==================Corrigir cadastro - CEST==========================================
        self.CorrgirCestScreen = QDockWidget(self.centralwidget)
        self.CorrgirCestScreen.hide()
        # ====================================================================================

        # ==================Corrigir cadastro - 0220==========================================
        self.Corrgir0220Screen = QDockWidget(self.centralwidget)
        self.Corrgir0220Screen.hide()
        # ====================================================================================

        # ==================XML em SPED=======================================================
        self.XMLinSPEDScreen = QDockWidget(self.centralwidget)
        self.XMLinSPEDScreen.hide()
        # ====================================================================================

        # ==================Calcular Quant ICMS Ressarcimento=================================
        self.Calc_Quant_ICMS_RessarScreen = QDockWidget(self.centralwidget)
        self.Calc_Quant_ICMS_RessarScreen.hide()
        # ====================================================================================

        # ==================Exportar Saldo Inicial - Tela=====================================
        self.ExportarSaldoInicialScreen = QDockWidget(self.centralwidget)
        self.ExportarSaldoInicialScreen.hide()
        # ====================================================================================

        # ==================Exportar Saldo Inicial - Tela=====================================
        self.FindXMlWithoutStScreen = QDockWidget(self.centralwidget)
        self.FindXMlWithoutStScreen.hide()
        # ====================================================================================

        # ==================Importar Cadatro produtis - Tela==================================
        self.CadstroProdutosScreen = QDockWidget(self.centralwidget)
        self.CadstroProdutosScreen.hide()
        # ====================================================================================

        # ==================Importar Registro H010- Tela======================================
        self.ImportarRegistroH010Screen = QDockWidget(self.centralwidget)
        self.ImportarRegistroH010Screen.hide()
        # ====================================================================================

        # ==================Importar Codigo de Relacionamento Tela============================
        self.ImportarCodigoRelacionamentoScreen = QDockWidget(self.centralwidget)
        self.ImportarCodigoRelacionamentoScreen.hide()
        # ====================================================================================

        # ====================================================================================
        self.actionAtivar_empresa = QtWidgets.QAction(MainWindow)
        self.actionAtivar_empresa.setObjectName("actionAtivar_empresa")
        self.actionAtivar_empresa.triggered.connect(
            lambda: self.handleAtiverEmpresa()
            )

        self.actionCadastrar = QtWidgets.QAction(MainWindow)
        self.actionCadastrar.setObjectName("actionCadastrar")
        self.actionCadastrar.triggered.connect(
            lambda: self.handleCadastrarEmpresa()
            )

        #====================Action Importar XML ====================================
        self.actionXML_Entrada = QtWidgets.QAction(MainWindow)
        self.actionXML_Entrada.setObjectName(
            "actionXML_Entrada")
        self.actionXML_Entrada.triggered.connect(
            lambda: self.handleImportarXML()
            )
        #===========================================================================

        #===================Action Editar===========================================
        self.actionEditar = QtWidgets.QAction(MainWindow)
        self.actionEditar.setObjectName("actionEditar")
        self.actionEditar.triggered.connect(
            lambda: self.handleEditarEmpresa()
        )
        #===========================================================================

        self.actionCodigo_de_relacionamento_2 = QtWidgets.QAction(MainWindow)
        self.actionCodigo_de_relacionamento_2.setObjectName(
            "actionCodigo_de_relacionamento_2")

        self.actionGerar_SPED_com_0220 = QtWidgets.QAction(MainWindow)
        self.actionGerar_SPED_com_0220.setObjectName(
            "actionGerar_SPED_com_0220")


        #====================SPED_Corrigir_CEST=======================================
        self.actionAdicionar_SPED_Corrigir_CEST = QtWidgets.QAction(MainWindow)
        self.actionAdicionar_SPED_Corrigir_CEST.setObjectName(
            "actionAdicionar_SPED_Corrigir_CEST")
        self.actionAdicionar_SPED_Corrigir_CEST.triggered.connect(
            lambda: self.handleCorrgirCest()
        )
        #=============================================================================

        #====================Action Registro C170 ====================================
        self.actionRegistro_C170_SPED = QtWidgets.QAction(MainWindow)
        self.actionRegistro_C170_SPED.setObjectName("actionRegistro_C170_SPED")
        self.actionRegistro_C170_SPED.triggered.connect(
            lambda: self.handleImportarC170()
            )
        #=============================================================================

        #====================Action adicionar 0220====================================
        self.actionAdicionar_registro_0220_no_SPED = QtWidgets.QAction(
            MainWindow)
        self.actionAdicionar_registro_0220_no_SPED.setObjectName(
            "actionAdicionar_registro_0220_no_SPED")
        self.actionAdicionar_registro_0220_no_SPED.triggered.connect(
            lambda: self.handleCorrgir0220()
        )
        #=============================================================================

        self.actionFator_de_convers_o = QtWidgets.QAction(MainWindow)
        self.actionFator_de_convers_o.setObjectName("actionFator_de_convers_o")

        # ======================Calcular SALDO INICIAL================================
        self.actionSaldo_inicial = QtWidgets.QAction(MainWindow)
        self.actionSaldo_inicial.setObjectName("actionSaldo_inicial")
        self.actionSaldo_inicial.triggered.connect(
            lambda: self.handleCalSaldoInicial()
        )
        # =============================================================================
        self.actionVerificarXMLInSPED = QtWidgets.QAction(MainWindow)
        self.actionVerificarXMLInSPED.setObjectName("actionactionVerificarXMLInSPED")
        self.actionVerificarXMLInSPED.triggered.connect(
            lambda: self.handleXMLInSPED()
        )

        # =========================Action calcular quant icms ressarcimento============
        self.actionCalcQuantICMSRessar = QtWidgets.QAction(MainWindow)
        self.actionCalcQuantICMSRessar.setObjectName("actionCalcQuantICMSRessar")
        self.actionCalcQuantICMSRessar.triggered.connect(
            lambda: self.handleCalcularICMSRessarcimento()
        )
        # =============================================================================


        # =========================Action Encontar XML sem ST============
        self.actionFindXMLWitoughtST = QtWidgets.QAction(MainWindow)
        self.actionFindXMLWitoughtST.setObjectName("actionFindXMLWitoughtST")
        self.actionFindXMLWitoughtST.triggered.connect(
            lambda: self.handleFindXMLWhithoughtST()
        )
        # =============================================================================

        # =========================Action Impoartar Cadastro produtos==================
        self.actionImportarCadastroProduto = QtWidgets.QAction(MainWindow)
        self.actionImportarCadastroProduto.setObjectName("actionImportarCadastroProduto")
        self.actionImportarCadastroProduto.triggered.connect(
            lambda: self.handleCadastroProdutos()
        )
        # =============================================================================

        # =========================Action importar Registro H010=======================
        self.actionImportarRegistroH010 = QtWidgets.QAction(MainWindow)
        self.actionImportarRegistroH010.setObjectName("actionImportarRegistroH010")
        self.actionImportarRegistroH010.triggered.connect(
            lambda: self.handleImportarRegistroH010()
        )
        # =============================================================================

        # =========================Action importar Codigo de Relacionamento============
        self.actionImportarCodigoRelacionamento = QtWidgets.QAction(MainWindow)
        self.actionImportarCodigoRelacionamento.setObjectName("actionImportarCodigoRelacionamento")
        self.actionImportarCodigoRelacionamento.triggered.connect(
            lambda: self.handleImportarCodigoRelacionamento()
        )
        # =============================================================================

        # ======================= Adicionar Ações no menu =============================


        self.menuEmpresa.addAction(self.actionAtivar_empresa)
        self.menuEmpresa.addAction(self.actionCadastrar)
        self.menuEmpresa.addAction(self.actionEditar)

        self.menuImportar.addAction(self.actionXML_Entrada)
        self.menuImportar.addAction(self.actionRegistro_C170_SPED)
        self.menuImportar.addAction(self.actionFator_de_convers_o)
        self.menuImportar.addAction(self.actionImportarCadastroProduto)
        self.menuImportar.addAction(self.actionImportarRegistroH010)
        self.menuImportar.addAction(self.actionImportarCodigoRelacionamento)

        self.menuExportar.addAction(self.actionCodigo_de_relacionamento_2)
        self.menuExportar.addAction(self.actionSaldo_inicial)

        self.menuAnalise.addAction(self.actionVerificarXMLInSPED)

        self.menuCorrecoes.addAction(self.actionAdicionar_SPED_Corrigir_CEST)
        self.menuCorrecoes.addAction(self.actionAdicionar_registro_0220_no_SPED)

        self.menuUteis.addAction(self.actionCalcQuantICMSRessar)
        self.menuUteis.addAction(self.actionFindXMLWitoughtST)

        self.menubar.addAction(self.menuEmpresa.menuAction())
        self.menubar.addAction(self.menuImportar.menuAction())
        self.menubar.addAction(self.menuExportar.menuAction())
        self.menubar.addAction(self.menuAnalise.menuAction())
        self.menubar.addAction(self.menuCorrecoes.menuAction())
        self.menubar.addAction(self.menuUteis.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ActiveCompany.setWhatsThis(_translate(
            "MainWindow", "<html><head/><body><p>Empresa ativa</p></body></html>"))
        self.menuEmpresa.setTitle(_translate("MainWindow", "Empresa"))
        self.menuImportar.setTitle(_translate("MainWindow", "Importar"))
        self.menuExportar.setTitle(_translate("MainWindow", "Exportar"))
        self.menuAnalise.setTitle(_translate("MainWindow", "Analises"))
        self.menuCorrecoes.setTitle(_translate("MainWindow", "Correções"))
        self.menuUteis.setTitle(_translate("MainWindow", "Uteis"))

        self.actionAtivar_empresa.setText(_translate("MainWindow", "Ativar"))
        self.actionCadastrar.setText(_translate("MainWindow", "Cadastrar"))
        self.actionXML_Entrada.setText(
            _translate("MainWindow", "XML Entrada"))

        self.actionEditar.setText(_translate("MainWindow", "Editar"))
        self.actionCodigo_de_relacionamento_2.setText(
            _translate("MainWindow", "Codigo de relacionamento"))

        self.actionGerar_SPED_com_0220.setText(_translate(
            "MainWindow", "Adicionar registro 0220 no SPED"))

        self.actionAdicionar_SPED_Corrigir_CEST.setText(
            _translate("MainWindow", "SPED - Corrigir CEST"))

        self.actionRegistro_C170_SPED.setText(
            _translate("MainWindow", "Registro C170 - SPED"))

        self.actionAdicionar_registro_0220_no_SPED.setText(
            _translate("MainWindow", "SPED - Adicionar 0220"))

        self.actionFator_de_convers_o.setText(
            _translate("MainWindow", "Fator de conversão"))

        self.actionSaldo_inicial.setText(
            _translate("MainWindow", "Saldo inicial"))

        self.actionVerificarXMLInSPED.setText(
            _translate("MainWindow", "Verificar XML em SPED"))

        self.actionCalcQuantICMSRessar.setText(
            _translate("MainWindow", "Calcular ICMS Ressarcimento"))

        self.actionFindXMLWitoughtST.setText(
            _translate("MainWindow", "Encontrar XML Transf S/ ST"))

        self.actionImportarCadastroProduto.setText(
            _translate("MainWindow", "Cadastro de Produtos"))

        self.actionImportarRegistroH010.setText(
            _translate("MainWindow", "Registro H010"))

        self.actionImportarCodigoRelacionamento.setText(
            _translate("MainWindow", "Codigo Relacionamento"))

    def handleAtiverEmpresa(self):
        AtivarFeature(
            self.AtivarEmpresaScreen,
            self.ActiveCompany,
            self.ActiveCNPJ
            )

    def handleCadastrarEmpresa(self):
        CadastrarFeature(self.CadastrarEmpresaScreen)

    def handleImportarXML(self):
        XMLFeature(
            self.ImportarXMLScreen,
            self.ActiveCNPJ,
            self.AlertScreen
            )

    def handleImportarC170(self):
        RegistroC170Feature(
            self.ImportarC170Screen,
            self.ActiveCNPJ
        )

    def handleCorrgirCest(self):
        CorrigirCestFeature(
            self.CorrgirCestScreen,
            self.ActiveCNPJ
        )

    def handleCorrgir0220(self):
        Corrigir0220Feature(
            self.Corrgir0220Screen,
            self.ActiveCNPJ
        )

    def handleEditarEmpresa(self):
        EditarFeature(
            self.EditarEmpresaScreen,
            self.ActiveCNPJ
        )

    def handleXMLInSPED(self):
        XMLInSPEDFeature(
            self.XMLinSPEDScreen,
            self.ActiveCNPJ
    )

    def handleCalcularICMSRessarcimento(self):
        CalcICMSRessarFeature(
            self.XMLinSPEDScreen,
            self.ActiveCNPJ
        )

    def handleCalSaldoInicial(self):
        SaldoInicialFeature(
            self.ExportarSaldoInicialScreen,
            self.ActiveCNPJ
        )

    def handleFindXMLWhithoughtST(self):
        FindXMlWithoutStFeature(
            self.FindXMlWithoutStScreen,
            self.ActiveCNPJ
        )

    def handleCadastroProdutos(self):
        ImportarCadastroProdutosFeature(
            self.FindXMlWithoutStScreen,
            self.ActiveCNPJ
        )

    def handleImportarRegistroH010(self):
        RegistroH010Feature(
            self.FindXMlWithoutStScreen,
            self.ActiveCNPJ
        )

    def handleImportarCodigoRelacionamento(self):
        ImportarCodigoRelacionamentoFeature(
            self.FindXMlWithoutStScreen,
            self.ActiveCNPJ
        )

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
