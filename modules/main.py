import dtlpy as dl


@dl.Package.defs.module()
class Runner(dl.BaseServiceRunner):
    def __init__(self):
        self.model = {}

    @dl.Package.defs.function(inputs={'item': dl.Item})
    def inference(self, item):
        return self.model.get('pred', item.name)

    @dl.Package.defs.function()
    def hello(self):
        return 'world'
