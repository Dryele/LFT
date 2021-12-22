from abc import abstractmethod
from abc import ABCMeta

class Inicio(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class Literal(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class CriarTabela(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class InserirDados(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class DadosInseridos(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class Tipo(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class Sufixo(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class TabelaColunas(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class Comando(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class Comandos(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class Procedure(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class Fetch(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class Set(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class Exec(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
  
class ListTypeId(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class ComposicaoCriarTabela(Inicio):
    def __init__(self, criarTabela, composicaoCriarTabela):
        self.criarTabela = criarTabela
        self.composicaoCriarTabela = composicaoCriarTabela
    def accept(self, Visitor):
       Visitor.visitComposicaoCriarTabela(self)

class ComposicaoInserirDados(Inicio):
    def __init__(self, inserirDados, composicaoInserirDados):
      self.inserirDados = inserirDados
      self.composicaoInserirDados = composicaoInserirDados
    def accept(self, Visitor):
       Visitor.visitComposicaoInserirDados(self)

class CriaTabela(CriarTabela):
    def __init__(self, ID, tabelacolunas):
        self.ID = ID
        self.tabelacolunas = tabelacolunas
    def accept(self, Visitor):
       Visitor.visitCriaTabela(self)

class InserirDados(InserirDados):
    def __init__(self, ID, dadosinseridos):
        self.ID = ID
        self.dadosinseridos = dadosinseridos
    def accept(self, Visitor):
       Visitor.visitInserirDados(self)

class ComposicaoDadosInseridos(DadosInseridos):
    def __init__(self, literal, ComposicaoDadosInseridos):
      self.literal = literal
      self.ComposicaoDadosInseridos = ComposicaoDadosInseridos
    def accept(self, Visitor):
       Visitor.visitComposicaoDadosInseridos(self)

class TipoInt(Tipo):
  def accept(self, Visitor):
    Visitor.visitTipoInt(self)

class TipoVarChar(Tipo):
  def accept(self, Visitor):
    Visitor.visitTipoVarchar(self)
  def __init__(self, numInteiro):
      self.numInteiro = numInteiro

class TipoNumeric(Tipo):  
  def accept(self, Visitor):
    Visitor.visitTipoNumeric(self)

class TipoDateTime(Tipo):
  def accept(self, Visitor):
    Visitor.visitTipoDateTime(self)

class TipoNumFloat(Tipo):
  def accept(self, Visitor):
    Visitor.visitTipoNumFloat(self)
   
class DeclareVar(Comando):
    def __init__(self, listtypedid):
        self.listtypedid = listtypedid
    def accept(self, Visitor):
       Visitor.visitDeclareVar(self)

class Deallocate(Comando):
    def __init__(self, ID):
        self.ID = ID
    def accept(self, Visitor):
       Visitor.visitDeallocate(self)

class While(Comando):
    def __init__(self, ID, comandos):
        self.ID = ID
        self.comandos = comandos
    def accept(self, Visitor):
       Visitor.visitWhile(self)

class Begin(Comando):
    def __init__(self, comandos):
        self.comandos = comandos
    def accept(self, Visitor):
       Visitor.visitBegin(self)
       
class BeginSet(Comando):
    def __init__(self,set, comandos):
        self.set = set
        self.comandos = comandos
    def accept(self, Visitor):
       Visitor.visitBeginSet(self)

class Procedure(Procedure):
    def __init__(self, ID, begin, comandos, close, deallocate):
        self.ID = ID
        self.begin = begin
        self.comandos = comandos
        self.close = close
        self.deallocate = deallocate
    def accept(self, Visitor):
       Visitor.visitProcedure(self)

class Open(Comando):
    def __init__(self, ID):
        self.ID = ID
    def accept(self, Visitor):
       Visitor.visitOpen(self)

class Close(Comando):
    def __init__(self, ID):
        self.ID = ID
    def accept(self, Visitor):
       Visitor.visitClose(self)

class Fetch(Fetch):
    def __init__(self, ID, dadossemtipo):
        self.ID = ID
        self.dadossemtipo = dadossemtipo
    def accept(self, Visitor):
       Visitor.visitFetch(self)

class Set(Set):
    def __init__(self, ID, select):
        self.ID = ID
        self.select = select
    def accept(self, Visitor):
       Visitor.visitSet(self)


class Exec(Exec):
    def __init__(self, ID, dadossemtipo):
        self.ID = ID
        self.dadossemtipo = dadossemtipo
    def accept(self, Visitor):
       Visitor.visitExec(self)

class NumFloat(Literal):
    def __init__(self, numfloat):
        self.numfloat = numfloat
    def accept(self, Visitor):
       Visitor.visitNumFloat(self)

class NumInteiro(Literal):
    def __init__(self, numInteiro):
     self.numInteiro = numInteiro
    def accept(self, Visitor):
     Visitor.visitNumInteiro(self) 

class String(Literal):
    def __init__(self, String):
      self.String = String
    def accept(self, Visitor):
      Visitor.visitString(self) 

class SufixoNotNull(Sufixo):
  def accept(self, Visitor):
    Visitor.visitSufixoNotNull(self)

class SufixoNull(Sufixo):
  def accept(self, Visitor):
    Visitor.visitSufixoNull(self)

class SufixoNotNullPrimaryKey(Sufixo):
  def accept(self, Visitor):
    Visitor.visitSufixoNotNullPrimaryKey(self)

class If(Comando):
    def __init__(self, ID, literal, begin, comando):
        self.ID = ID
        self.literal = literal
        self.begin = begin
        self.comando = comando
    def accept(self, Visitor):
       Visitor.visitIf(self)

class IfElif(Comando):
    def __init__(self, IDIf, literalIf, beginIf, comandoIf, IDElif, literalElif, beginElif, comandoElif):
        self.IDIf = IDIf
        self.literalIf = literalIf
        self.beginIf = beginIf
        self.comandoIf = comandoIf
        self.IDElif = IDElif
        self.literalElif = literalElif
        self.beginElif = beginElif
        self.comandoElif = comandoElif
    def accept(self, Visitor):
       Visitor.visitElif(self)

class IfElse(Comando):
    def __init__(self, IDIf, literalIf, beginIf, comandoIf, beginElse, comandoElse):
        self.IDIf = IDIf
        self.literalIf = literalIf
        self.beginIf = beginIf
        self.comandoIf = comandoIf
        self.beginElse = beginElse
        self.comandoElse = comandoElse
    def accept(self, Visitor):
       Visitor.visitIfElse(self)

class Comandos(Comandos):
    def __init__(self, comando):
        self.comando = comando
    def accept(self, Visitor):
       Visitor.visitComandos(self)

class ComandosComando(Comandos):
    def __init__(self,comando, comandos):
        self.comando = comando
        self.comandos = comandos
    def accept(self, Visitor):
       Visitor.visitComandosComandos(self)

class ComposicaoDadosSemTipo(Comandos):
    def __init__(self, ID, ComposicaoDadosSemTipo):
        self.ID = ID
        self.ComposicaoDadosSemTipo = ComposicaoDadosSemTipo
    def accept(self, Visitor):
       Visitor.visitComposicaoDadosSemTipo(self)

class SelectMul(Comando):
    def __init__(self, ID):
        self.ID = ID
    def accept(self, Visitor):
        Visitor.visitSelectMul(self)
  
class SelectSum(Comando):
    def __init__(self, ID1, ID2, ID3, ID4):
        self.ID1 = ID1
        self.ID2 = ID2
        self.ID3 = ID3
        self.ID4 = ID4
    def accept(self, Visitor):
        Visitor.visitSelectSum(self)

class SelectTypedId(Comando):
    def __init__(self, listtypedid, ID):
        self.listtypedid = listtypedid
        self.ID = ID
    def accept(self, Visitor):
        Visitor.visitSelectTypedId(self)

class ListTypeIdSimples(ListTypeId):
    def  __init__(self, ID, tipo):
         self.ID = ID
         self.tipo = tipo
    def accept(self, Visitor):
        Visitor.visitListTypeIdSimples(self)
      
class ListTypeIdComposto(ListTypeId):
    def __init__(self, ID, tipo, listtypeid):
        self.ID = ID
        self.tipo = tipo
        self.listtypedid = listtypeid
    def accept(self, Visitor):
        Visitor.visitListTypeIdComposto(self)

class TabelaColunasSimples(TabelaColunas):
  def __init__(self, ID, tipo, sufixotable):
      self.ID = ID
      self.tipo = tipo
      self.sufixotable = sufixotable
  def accept(self, Visitor):
      Visitor.visitTabelaColunasSimples(self)

class TabelaColunasComposta(TabelaColunas):
  def __init__(self, ID, tipo, sufixotable, tabelacolunas):
      self.ID = ID
      self.tipo = tipo
      self.sufixotable = sufixotable
      self.tabelacolunas = tabelacolunas
  def accept(self, Visitor):
      Visitor.visitTabelaColunasComposta(self)