#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri Apr 20 19:17:35 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from bokeh.client import push_session
from bokeh.plotting import curdoc
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import bokehgui
import functools
import osmosdr
import signal
import time

class top_block(gr.top_block):
    def __init__(self, doc):
        gr.top_block.__init__(self, "Top Block")
        self.doc = doc
        self.plot_lst = []
        self.widget_lst = []

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2e6
        self.center_freq = center_freq = 100

        ##################################################
        # Blocks
        ##################################################

        self.center_freq_slider = bokehgui.slider(self.widget_lst, "center_freq"+":", 60, 160, 0.1, 1, 100)
        self.center_freq_slider.add_callback(lambda attr, old, new: self.set_center_freq(new))

        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq((center_freq)*1e6, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(40, 0)
        self.osmosdr_source_0.set_if_gain(0, 0)
        self.osmosdr_source_0.set_bb_gain(0, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        self.bokehgui_frequency_sink_x_0 = bokehgui.freq_sink_c_proc(2072,
                             firdes.WIN_BLACKMAN_hARRIS,
                             center_freq, 10,
                             "", 1)
        self.bokehgui_frequency_sink_x_0_plot = bokehgui.freq_sink_c(self.doc, self.plot_lst, self.bokehgui_frequency_sink_x_0, is_message = False)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        legend_list = []

        for i in xrange(1):
            if len(labels[i]) == 0:
                legend_list.append("Data {0}".format(i))
            else:
                legend_list.append(labels[i])

        self.bokehgui_frequency_sink_x_0_plot.initialize(update_time = 100,
                                   legend_list = legend_list)

        self.bokehgui_frequency_sink_x_0_plot.set_y_axis([-140, -20])
        self.bokehgui_frequency_sink_x_0_plot.set_y_label('Relative Gain' + '(' +'dB'+')')
        self.bokehgui_frequency_sink_x_0_plot.set_x_label('Frequency' + '(' +"Mhz"+')')

        self.bokehgui_frequency_sink_x_0_plot.set_trigger_mode(bokehgui.TRIG_MODE_FREE,0.0, 0, "")

        self.bokehgui_frequency_sink_x_0_plot.enable_grid(True)
        self.bokehgui_frequency_sink_x_0_plot.enable_axis_labels(True)
        self.bokehgui_frequency_sink_x_0_plot.disable_legend(not True)
        self.bokehgui_frequency_sink_x_0_plot.set_layout(*(((1,0))))
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        styles = ["solid", "solid", "solid", "solid", "solid",
                  "solid", "solid", "solid", "solid", "solid"]
        markers = [None, None, None, None, None,
                   None, None, None, None, None]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            self.bokehgui_frequency_sink_x_0_plot.format_line(i, colors[i], widths[i], styles[i], markers[i], alphas[i])


        if self.widget_lst:
            input_t = bokehgui.BokehLayout.widgetbox(self.widget_lst)
            widgetbox = bokehgui.BokehLayout.WidgetLayout(input_t)
            widgetbox.set_layout(*((0, 0)))
            list_obj = [widgetbox] + self.plot_lst
        else:
            list_obj = self.plot_lst
        layout_t = bokehgui.BokehLayout.create_layout(list_obj, "fixed")
        self.doc.add_root(layout_t)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.osmosdr_source_0, 0), (self.bokehgui_frequency_sink_x_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.osmosdr_source_0.set_center_freq((self.center_freq)*1e6, 0)
        self.bokehgui_frequency_sink_x_0.set_frequency_range(self.center_freq, 10)


def main(top_block_cls=top_block, options=None):

    serverProc, port = bokehgui.utils.create_server()
    def killProc(signum, frame, tb):
        tb.stop()
        tb.wait()
        serverProc.terminate()
        serverProc.kill()
    time.sleep(6)
    try:
        # Define the document instance
        doc = curdoc()
        doc.title = "Top Block"
        session = push_session(doc, session_id="top_block",
                               url = "http://localhost:" + port + "/bokehgui")
        # Create Top Block instance
        tb = top_block_cls(doc)
        try:
            tb.start()
            signal.signal(signal.SIGTERM, functools.partial(killProc, tb=tb))
            session.loop_until_closed()
        finally:
            print "Exiting the simulation. Stopping Bokeh Server"
            tb.stop()
            tb.wait()
    finally:
        serverProc.terminate()
        serverProc.kill()


if __name__ == '__main__':
    main()
