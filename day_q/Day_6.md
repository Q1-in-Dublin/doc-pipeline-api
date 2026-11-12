1.class와 그걸로 만든 **객체(인스턴스)**는 어떻게 다른가요?
=> Class는 객체를 만드는 blueprint이고 객체는 실제 구현체 2.**init**과 self는 각각 뭘 하나요?
=> **init**은 magic method로서 이 초기화 담당(Attribute setting), self는 객체 그자신
@dataclass를 붙이면 무엇을 자동으로 만들어 주나요?
=> magic method dunder
@dataclass(frozen=True)는 무슨 뜻이고, Day 1에 배운 무엇과 연결되나요?
frozen=True는 객체를 만든 뒤 필드에 값을 다시 대입하는 걸 막는다. Day 1의 immutable → hashable과 연결된다. 값이 안 바뀌니 hash도 안 바뀌어서 dict 키나 set 원소로 쓸 수 있다. 다만 tuple 안의 list처럼 필드가 list면 그 안쪽은 바뀔 수 있고, 그때는 hashable이 아니다.

두 객체를 ==로 비교하면 일반 클래스와 dataclass에서 결과가 어떻게 다른가요?
일반class에서는 같은 객체인지를 비교한다. False
Dataclass객체에서는 필드값이 같은지를 비교한다. True로나온다
