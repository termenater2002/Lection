class MixinSpeakable:
    def speak():
        print("я базарю")
        
class MixinAnimated:
    dance: bool = False
    def is_animated(self):
        print(f"я танцую и это {self.dance}")
        
class MixinFunny:
    def make_laugh():
        print("я иду на СВО")
        
class BaseCharaster(MixinSpeakable, MixinAnimated, MixinFunny):
    name: str
    persona1: str = "GAY"

