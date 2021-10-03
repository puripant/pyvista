"""Test any plotting that does not require rendering.

All other tests requiring rendering should to in
./plotting/test_plotting.py

"""
import pytest
import pyvista


def test_plotter_image():
    plotter = pyvista.Plotter()
    with pytest.raises(AttributeError, match='not yet been setup'):
        plotter.image


def test_enable_hidden_line_removal():
    plotter = pyvista.Plotter(shape=(1, 2))
    plotter.enable_hidden_line_removal(False)
    assert plotter.renderers[0].GetUseHiddenLineRemoval()
    assert not plotter.renderers[1].GetUseHiddenLineRemoval()

    plotter.enable_hidden_line_removal(True)
    assert plotter.renderers[1].GetUseHiddenLineRemoval()


def test_disable_hidden_line_removal():
    plotter = pyvista.Plotter(shape=(1, 2))
    plotter.enable_hidden_line_removal(True)

    plotter.disable_hidden_line_removal(False)
    assert not plotter.renderers[0].GetUseHiddenLineRemoval()
    assert plotter.renderers[1].GetUseHiddenLineRemoval()

    plotter.disable_hidden_line_removal(True)
    assert not plotter.renderers[1].GetUseHiddenLineRemoval()


def test_add_legend_no_face(sphere):
    pl = pyvista.Plotter()
    pl.add_mesh(sphere, label='sphere')
    pl.add_legend(face=None)

    pl = pyvista.Plotter()
    pl.add_mesh(sphere)
    pl.add_legend(labels=[['sphere', 'k']], face=None)


def test_add_remove_legend(sphere):
    pl = pyvista.Plotter()
    pl.add_mesh(sphere, label='sphere')
    pl.add_legend()
    pl.remove_legend()
