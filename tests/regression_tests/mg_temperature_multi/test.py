import os

import numpy as np
import openmc
import openmc.mgxs

from tests.testing_harness import PyAPITestHarness


def create_library():
    # Instantiate the energy group data
    egroups = [1e-5, 0.0635, 10.0, 1.0e2, 1.0e3, 0.5e6, 1.0e6, 20.0e6]
    groups = openmc.mgxs.EnergyGroups(egroups)

    # Instantiate the 7-group (C5G7) cross section data
    uo2_xsdata = openmc.XSdata('UO2', groups, temperatures=[294.0, 600.0])
    uo2_xsdata.order = 0
    scatter_matrix = np.array([[
        [0.1275370, 0.0423780, 0.0000094, 0.0000000, 0.0000000, 0.0000000, 0.0000000],
        [0.0000000, 0.3244560, 0.0016314, 0.0000000, 0.0000000, 0.0000000, 0.0000000],
        [0.0000000, 0.0000000, 0.4509400, 0.0026792, 0.0000000, 0.0000000, 0.0000000],
        [0.0000000, 0.0000000, 0.0000000, 0.4525650, 0.0055664, 0.0000000, 0.0000000],
        [0.0000000, 0.0000000, 0.0000000, 0.0001253, 0.2714010, 0.0102550, 0.0000000],
        [0.0000000, 0.0000000, 0.0000000, 0.0000000, 0.0012968, 0.2658020, 0.0168090],
        [0.0000000, 0.0000000, 0.0000000, 0.0000000, 0.0000000, 0.0085458, 0.2730800]
    ]])
    scatter_matrix = np.rollaxis(scatter_matrix, 0, 3)

    # Original C5G7 data
    uo2_xsdata.set_total([0.1779492, 0.3298048, 0.4803882, 0.5543674, 0.3118013, 0.3951678, 0.5644058], temperature=294.0)
    uo2_xsdata.set_absorption([8.0248E-03, 3.7174E-03, 2.6769E-02, 9.6236E-02, 3.0020E-02, 1.1126E-01, 2.8278E-01], temperature=294.0)
    uo2_xsdata.set_scatter_matrix(scatter_matrix, temperature=294.0)
    uo2_xsdata.set_fission([7.21206E-03, 8.19301E-04, 6.45320E-03, 1.85648E-02, 1.78084E-02, 8.30348E-02, 2.16004E-01], temperature=294.0)
    uo2_xsdata.set_nu_fission([2.005998E-02, 2.027303E-03, 1.570599E-02, 4.518301E-02, 4.334208E-02, 2.020901E-01, 5.257105E-01], temperature=294.0)
    uo2_xsdata.set_chi([5.8791E-01, 4.1176E-01, 3.3906E-04, 1.1761E-07, 0.0000E+00, 0.0000E+00, 0.0000E+00], temperature=294.0)

    # Altered C5G7 data (permuted Chi)
    uo2_xsdata.set_total([0.1779492, 0.3298048, 0.4803882, 0.5543674, 0.3118013, 0.3951678, 0.5644058], temperature=600.0)
    uo2_xsdata.set_absorption([8.0248E-03, 3.7174E-03, 2.6769E-02, 9.6236E-02, 3.0020E-02, 1.1126E-01, 2.8278E-01], temperature=600.0)
    uo2_xsdata.set_scatter_matrix(scatter_matrix, temperature=600.0)
    uo2_xsdata.set_fission([7.21206E-03, 8.19301E-04, 6.45320E-03, 1.85648E-02, 1.78084E-02, 8.30348E-02, 2.16004E-01], temperature=600.0)
    uo2_xsdata.set_nu_fission([2.005998E-02, 2.027303E-03, 1.570599E-02, 4.518301E-02, 4.334208E-02, 2.020901E-01, 5.257105E-01], temperature=600.0)
    uo2_xsdata.set_chi([4.1176E-01, 5.8791E-01, 3.3906E-04, 1.1761E-07, 0.0000E+00, 0.0000E+00, 0.0000E+00], temperature=600.0)

    h2o_xsdata = openmc.XSdata('LWTR', groups)
    h2o_xsdata.order = 0
    h2o_xsdata.set_total([0.15920605, 0.412969593, 0.59030986, 0.58435,
                          0.718, 1.2544497, 2.650379])
    h2o_xsdata.set_absorption([6.0105E-04, 1.5793E-05, 3.3716E-04,
                               1.9406E-03, 5.7416E-03, 1.5001E-02,
                               3.7239E-02])
    scatter_matrix = np.array([[
        [0.0444777, 0.1134000, 0.0007235, 0.0000037, 0.0000001, 0.0000000, 0.0000000],
        [0.0000000, 0.2823340, 0.1299400, 0.0006234, 0.0000480, 0.0000074, 0.0000010],
        [0.0000000, 0.0000000, 0.3452560, 0.2245700, 0.0169990, 0.0026443, 0.0005034],
        [0.0000000, 0.0000000, 0.0000000, 0.0910284, 0.4155100, 0.0637320, 0.0121390],
        [0.0000000, 0.0000000, 0.0000000, 0.0000714, 0.1391380, 0.5118200, 0.0612290],
        [0.0000000, 0.0000000, 0.0000000, 0.0000000, 0.0022157, 0.6999130, 0.5373200],
        [0.0000000, 0.0000000, 0.0000000, 0.0000000, 0.0000000, 0.1324400, 2.4807000]
    ]])
    scatter_matrix = np.rollaxis(scatter_matrix, 0, 3)
    h2o_xsdata.set_scatter_matrix(scatter_matrix)

    mg_cross_sections_file = openmc.MGXSLibrary(groups)
    mg_cross_sections_file.add_xsdatas([uo2_xsdata, h2o_xsdata])
    mg_cross_sections_file.export_to_hdf5()


class MGXSTestHarness(PyAPITestHarness):
    def _cleanup(self):
        super()._cleanup()
        f = 'mgxs.h5'
        if os.path.exists(f):
            os.remove(f)


def test_mg_temperature_multi():
    ###############################################################################
    # Create multigroup data
    create_library()

    ###############################################################################
    # Create materials for the problem

    # Instantiate some Macroscopic Data
    uo2_data = openmc.Macroscopic('UO2')
    h2o_data = openmc.Macroscopic('LWTR')

    # Instantiate some Materials and register the appropriate Macroscopic objects
    uo2 = openmc.Material(name='UO2 fuel')
    uo2.set_density('macro', 1.0)
    uo2.add_macroscopic(uo2_data)

    water = openmc.Material(name='Water')
    water.set_density('macro', 1.0)
    water.add_macroscopic(h2o_data)

    # Instantiate a Materials collection and export to XML
    materials = openmc.Materials([uo2, water])
    materials.cross_sections = "mgxs.h5"

    ###############################################################################
    # Define problem geometry

    # Create a surface for the fuel outer radius
    fuel_ir = openmc.ZCylinder(r=0.25, name='Fuel IR')
    fuel_or = openmc.ZCylinder(r=0.54, name='Fuel OR')

    # Create a region represented as the inside of a rectangular prism
    pitch = 1.26
    box = openmc.rectangular_prism(pitch, pitch, boundary_type='reflective')

    # Instantiate Cells
    fuel_inner = openmc.Cell(fill=uo2, region=-fuel_ir, name='fuel inner')
    fuel_inner.temperature = 600.0
    fuel_outer = openmc.Cell(fill=uo2, region=+fuel_ir & -fuel_or, name='fuel outer')
    fuel_outer.temperature = 294.0
    moderator = openmc.Cell(fill=water, region=+fuel_or & box, name='moderator')

    # Create a geometry with the two cells and export to XML
    geometry = openmc.Geometry([fuel_inner, fuel_outer, moderator])

    ###############################################################################
    # Define problem settings

    # Instantiate a Settings object, set all runtime parameters, and export to XML
    settings = openmc.Settings()
    settings.energy_mode = "multi-group"
    settings.batches = 10
    settings.inactive = 5
    settings.particles = 1000

    # Create an initial uniform spatial source distribution over fissionable zones
    lower_left = (-pitch/2, -pitch/2, -1)
    upper_right = (pitch/2, pitch/2, 1)
    uniform_dist = openmc.stats.Box(lower_left, upper_right, only_fissionable=True)
    settings.source = openmc.IndependentSource(space=uniform_dist)

    ###############################################################################
    # Define tallies

    # Instantiate the energy group data
    egroups = [1e-5, 0.0635, 10.0, 1.0e2, 1.0e3, 0.5e6, 1.0e6, 20.0e6]

    inner_filter = openmc.CellFilter(fuel_inner)
    outer_filter = openmc.CellFilter(fuel_outer)
    energy_filter = openmc.EnergyFilter(egroups)

    inner_tally = openmc.Tally(name="inner tally")
    inner_tally.filters = [energy_filter]
    inner_tally.filters = [inner_filter]
    inner_tally.scores = ['flux']

    outer_tally = openmc.Tally(name="outer tally")
    outer_tally.filters = [energy_filter]
    outer_tally.filters = [outer_filter]
    outer_tally.scores = ['flux']

    # Instantiate a Tallies collection and export to XML
    tallies = openmc.Tallies([inner_tally, outer_tally])

    # Generate model and run test
    model = openmc.Model(geometry, materials, settings, tallies)

    harness = MGXSTestHarness('statepoint.10.h5', model=model)
    harness.main()
