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

class DadosInseridosUm(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class DadosInseridosDois(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class Tipo(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass


class SufixoTable(metaclass=ABCMeta):
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

class DeclareVar(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class Comandos(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class Select(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class Deallocate(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class ListTypeid(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass
      
class DadosSemTipo(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class While(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class Procedure(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class Open(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class Close(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class Fetch(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class Begin(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class Set(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class If(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class Exec(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass


class CriaTabelaInicio(Inicio):
    def __init__(self, criatabela1):
        self.criatabela1 = criatabela1
    def accept(self, Visitor):
       Visitor.visitCriaTabelaInicio(self)

class InserirDadosInicio(Inicio):
    def __init__(self, inseredados):
      self.inseredados = inseredados
    def accept(self, Visitor):
       Visitor.visitInserirDadosInicio(self)


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

class DadosInseridosUm(DadosInseridosUm):
    def __init__(self, literal):
        self.literal = literal
    def accept(self, Visitor):
       Visitor.visitDadosInseridosUm(self)

class DadosInseridosDois(DadosInseridosDois):
    def __init__(self, literal, dadosinseridos):
        self.literal = literal
        self.dadosinseridos = dadosinseridos
    def accept(self, Visitor):
       Visitor.visitDadosInseridosDois(self)
       
class DeclareVar(DeclareVar):
    def __init__(self, listtypedid):
        self.listtypedid = listtypedid
    def accept(self, Visitor):
       Visitor.visitDeclareVar(self)

class Deallocate(Deallocate):
    def __init__(self, ID):
        self.ID = ID
    def accept(self, Visitor):
       Visitor.visitDeallocate(self)

class While(While):
    def __init__(self, ID, comandos):
        self.ID = ID
        self.comandos = comandos
    def accept(self, Visitor):
       Visitor.visitWhile(self)

class Procedure(Procedure):
    def __init__(self, ID, begin, comandos, close, deallocate):
        self.ID = ID
        self.begin = begin
        self.comandos = comandos
        self.close = close
        self.deallocate = deallocate
    def accept(self, Visitor):
       Visitor.visitProcedure(self)

class Open(Open):
    def __init__(self, ID):
        self.ID = ID
    def accept(self, Visitor):
       Visitor.visitOpen(self)

class Close(Close):
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


