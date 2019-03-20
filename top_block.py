#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sat Dec 22 18:34:35 2018
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr
import sip
import sys
import time
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.working_samp_rate = working_samp_rate = 400e3
        self.transition_width = transition_width = 10e3
        self.samp_rate = samp_rate = 8e6
        self.freq_tx = freq_tx = 98e6
        self.channel_width = channel_width = 150e3
        self.center_freq = center_freq = 100e6
        self.audio_transition = audio_transition = 2e3
        self.audio_samp_rate = audio_samp_rate = 48e3
        self.audio_cutoff = audio_cutoff = 20e3

        ##################################################
        # Blocks
        ##################################################
        self._freq_tx_tool_bar = Qt.QToolBar(self)
        self._freq_tx_tool_bar.addWidget(Qt.QLabel('Transmit Frequency'+": "))
        self._freq_tx_line_edit = Qt.QLineEdit(str(self.freq_tx))
        self._freq_tx_tool_bar.addWidget(self._freq_tx_line_edit)
        self._freq_tx_line_edit.returnPressed.connect(
        	lambda: self.set_freq_tx(eng_notation.str_to_num(str(self._freq_tx_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._freq_tx_tool_bar)
        self.rational_resampler_2 = filter.rational_resampler_ccc(
                interpolation=int(samp_rate/working_samp_rate),
                decimation=1,
                taps=(firdes.low_pass(1, samp_rate, channel_width/2, transition_width)),
                fractional_bw=None,
        )
        self.rational_resampler_1 = filter.rational_resampler_fff(
                interpolation=int(working_samp_rate/audio_samp_rate),
                decimation=1,
                taps=(firdes.low_pass(1, working_samp_rate, audio_cutoff, audio_transition)),
                fractional_bw=None,
        )
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	center_freq, #fc
        	samp_rate, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_win)

        self.qtgui_sink_x_0.enable_rf_freq(True)



        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(100e6, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(10, 0)
        self.osmosdr_sink_0.set_if_gain(20, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)

        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/erik/Code/gnu-radio/fm_tx/HumanEvents_s32k.wav', True)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.analog_wfm_tx_0 = analog.wfm_tx(
        	audio_rate=int(working_samp_rate),
        	quad_rate=int(working_samp_rate),
        	tau=75e-6,
        	max_dev=75e3,
        	fh=-1.0,
        )
        self.analog_sig_source = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, freq_tx - center_freq, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_wfm_tx_0, 0), (self.rational_resampler_2, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.rational_resampler_1, 0))
        self.connect((self.rational_resampler_1, 0), (self.analog_wfm_tx_0, 0))
        self.connect((self.rational_resampler_2, 0), (self.blocks_multiply_xx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_working_samp_rate(self):
        return self.working_samp_rate

    def set_working_samp_rate(self, working_samp_rate):
        self.working_samp_rate = working_samp_rate
        self.rational_resampler_1.set_taps((firdes.low_pass(1, self.working_samp_rate, self.audio_cutoff, self.audio_transition)))

    def get_transition_width(self):
        return self.transition_width

    def set_transition_width(self, transition_width):
        self.transition_width = transition_width
        self.rational_resampler_2.set_taps((firdes.low_pass(1, self.samp_rate, self.channel_width/2, self.transition_width)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.rational_resampler_2.set_taps((firdes.low_pass(1, self.samp_rate, self.channel_width/2, self.transition_width)))
        self.qtgui_sink_x_0.set_frequency_range(self.center_freq, self.samp_rate)
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source.set_sampling_freq(self.samp_rate)

    def get_freq_tx(self):
        return self.freq_tx

    def set_freq_tx(self, freq_tx):
        self.freq_tx = freq_tx
        Qt.QMetaObject.invokeMethod(self._freq_tx_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.freq_tx)))
        self.analog_sig_source.set_frequency(self.freq_tx - self.center_freq)

    def get_channel_width(self):
        return self.channel_width

    def set_channel_width(self, channel_width):
        self.channel_width = channel_width
        self.rational_resampler_2.set_taps((firdes.low_pass(1, self.samp_rate, self.channel_width/2, self.transition_width)))

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.qtgui_sink_x_0.set_frequency_range(self.center_freq, self.samp_rate)
        self.analog_sig_source.set_frequency(self.freq_tx - self.center_freq)

    def get_audio_transition(self):
        return self.audio_transition

    def set_audio_transition(self, audio_transition):
        self.audio_transition = audio_transition
        self.rational_resampler_1.set_taps((firdes.low_pass(1, self.working_samp_rate, self.audio_cutoff, self.audio_transition)))

    def get_audio_samp_rate(self):
        return self.audio_samp_rate

    def set_audio_samp_rate(self, audio_samp_rate):
        self.audio_samp_rate = audio_samp_rate

    def get_audio_cutoff(self):
        return self.audio_cutoff

    def set_audio_cutoff(self, audio_cutoff):
        self.audio_cutoff = audio_cutoff
        self.rational_resampler_1.set_taps((firdes.low_pass(1, self.working_samp_rate, self.audio_cutoff, self.audio_transition)))


def main(top_block_cls=top_block, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
