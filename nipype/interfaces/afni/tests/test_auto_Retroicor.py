# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.afni.preprocess import Retroicor
def test_Retroicor_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    out_file=dict(position=1,
    mandatory=True,
    argstr='-prefix %s',
    ),
    resp=dict(position=-3,
    argstr='-resp %s',
    ),
    args=dict(argstr='%s',
    ),
    outputtype=dict(),
    cardphase=dict(position=-6,
    hash_files=False,
    argstr='-cardphase %s',
    ),
    respphase=dict(position=-7,
    hash_files=False,
    argstr='-respphase %s',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(position=-1,
    mandatory=True,
    argstr='%s',
    ),
    threshold=dict(position=-4,
    argstr='-threshold %d',
    ),
    order=dict(position=-5,
    argstr='-order %s',
    ),
    card=dict(position=-2,
    argstr='-card %s',
    ),
    )
    inputs = Retroicor.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_Retroicor_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = Retroicor.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
