from xai_components.base import InArg, OutArg, InCompArg, Component, BaseComponent, xai_component, SubGraphExecutor, \
    dynalist, secret

from switchbot import SwitchBot


@xai_component
class SwitchBotAuthorize(Component):
    token: InCompArg[secret]
    secret: InCompArg[secret]

    def execute(self, ctx) -> None:
        ctx['switchbot'] = SwitchBot(token=self.token.value, secret=self.secret.value)

@xai_component
class SwitchBotDevices(Component):
    devices: OutArg[list]

    def execute(self, ctx) -> None:
        switchbot = ctx['switchbot']
        self.devices.value = switchbot.devices()

@xai_component
class SwitchBotGetDevice(Component):
    id: InCompArg[str]    
    device: OutArg[any]

    def execute(self, ctx) -> None:
        switchbot = ctx['switchbot']
        self.device.value = switchbot.device(id=self.id.value)


@xai_component
class SwitchBotGetStatus(Component):
    device: InCompArg[any]

    status: OutArg[dict]

    def execute(self, ctx) -> None:
        self.status.value = self.device.value.status()


@xai_component
class SwitchBotTurnOn(Component):
    device: InCompArg[any]

    def execute(self, ctx) -> None:
        self.device.value.command('turn_on')

@xai_component
class SwitchBotTurnOff(Component):
    device: InCompArg[any]

    def execute(self, ctx) -> None:
        self.device.value.command('turn_off')


@xai_component
class SwitchBotPress(Component):
    device: InCompArg[any]

    def execute(self, ctx) -> None:
        self.device.value.command('press')


@xai_component
class SwitchBotSetPosition(Component):
    device: InCompArg[any]
    parameter: InCompArg[str]

    def execute(self, ctx) -> None:
        self.device.value.command('set_position', parameter=self.parameter.value)
