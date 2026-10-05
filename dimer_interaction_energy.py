"""Counterpoise-corrected Psi4 interaction energy at supplied fragment geometry."""
from common import *

def main():
    p=parser(__doc__); p.add_argument('fragment_a_xyz'); p.add_argument('fragment_b_xyz')
    p.add_argument('--charges',type=int,nargs=2,default=[0,0])
    p.add_argument('--method',default='b3lyp-d3bj/def2-tzvp')
    p.add_argument('--threads',type=int,default=4); p.add_argument('--memory',default='4 GB')
    a=p.parse_args(); out=output_dir(a)
    import psi4
    if a.threads<1: p.error('threads must be positive')
    body1=read_xyz(a.fragment_a_xyz); body2=read_xyz(a.fragment_b_xyz)
    psi4.set_num_threads(a.threads); psi4.set_memory(a.memory)
    psi4.core.set_output_file(str(out/'psi4.log'),False)
    mol=psi4.geometry(f'{a.charges[0]} 1\n{body1}\n--\n{a.charges[1]} 1\n{body2}\nunits angstrom\nsymmetry c1\nno_reorient\nno_com')
    psi4.set_options({'reference':'rhf','scf_type':'df','e_convergence':1e-9})
    energy=psi4.energy(a.method,molecule=mol,bsse_type='cp')
    dump(out/'interaction.json',dict(counterpoise_interaction_hartree=float(energy),
        counterpoise_interaction_kj_mol=float(energy)*HARTREE_KJ,method=a.method,
        warning='Closed-shell fragments only; use common coordinates from a meaningful dimer (do not overlap separately centred XYZs). Pair binding is not formation free energy; molecular deformation and many-body/packing effects excluded.'))

if __name__ == '__main__': main()
