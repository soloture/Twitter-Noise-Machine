s.boot;

(
SynthDef( \sin,	{ | amp = 0.01, freq = 333, interval = 2 |
	var sin;
	//env = EnvGen.kr( Env.asr( 0.001, 0.9, 0.001 ), trig, doneAction: 0 );
	//sig = LFTri.ar( [ freq, freq * 0.999 ], 0.0, amp ) * env;
	sin = Mix.new([SinOsc.ar(freq, 0, 0.2), SinOsc.ar(freq + interval, 0.5,0.2),SinOsc.ar(freq + interval * 2, 0.5,0.2),SinOsc.ar(freq + interval *3, 0.5,0.2)]);

	Out.ar( [ 0 ], sin * 0.6 );
}).add;

SynthDef( \background, { | amp = 1, freq = 100 |
	var n = 8, mix, ampOSC;
	ampOSC = SinOsc.kr(amp,0,0.8,0.5);
	mix = Mix.fill(n, { SinOsc.ar(100 + 100.0.rand, 0, (1 / n)) }) * ampOSC ;
	Out.ar([0], mix);
}).add;

j = Synth( \background );
h = Synth( \sin, [ \amp, 0.4 ,\freq, 10 ] );

x = OSCFunc( { | msg, time, addr, port |
	var pyFreq;

	pyFreq = msg[1].asFloat;
	( "tweet is " + pyFreq ).postln;
	( msg[0] ).postln;
	j.set( \amp, pyFreq );
}, '/tweets' );

x = OSCFunc( { | msg, time, addr, port |
	var pyFreq;

	pyFreq = msg[1].asFloat;
	( "freq is " + pyFreq ).postln;
	( msg[0] ).postln;
	h.set( \freq, pyFreq );
}, '/words' );
)

