from pyforms.basewidget import BaseWidget
from pyforms.controls   import ControlFile
from pyforms.controls   import ControlText
from pyforms.controls   import ControlSlider
from pyforms.controls   import ControlPlayer
from pyforms.controls   import ControlButton
#pip install PyForms-GUI
class ComputerVisionAlgorithm(BaseWidget):

    def __init__(self, *args, **kwargs):
        super().__init__('Computer vision algorithm example')

        self.set_margin(10)

        self._videofile  = ControlFile('Video')
        self._outputfile = ControlText('Results output file')
        self._threshold  = ControlSlider('Threshold', default=114, minimum=0, maximum=255)
        self._blobsize   = ControlSlider('Minimum blob size', default=110, minimum=100, maximum=2000)
        self._player     = ControlPlayer('Player')
        self._runbutton  = ControlButton('Run')

        self._videofile.changed_event     = self.__videoFileSelectionEvent
        self._runbutton.value       = self.__runEvent
        self._player.process_frame_event    = self.__process_frame
        self._formset = [
            ('_videofile', '_outputfile'),
            '_threshold',
            ('_blobsize', '_runbutton'),
            '_player'
        ]


    def __videoFileSelectionEvent(self):
        self._player.value = self._videofile.value

    def __process_frame(self, frame):
        return frame

    def __runEvent(self):"
        pass


if __name__ == '__main__':

    from pyforms import start_app
    start_app(ComputerVisionAlgorithm)
