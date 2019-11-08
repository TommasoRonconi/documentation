#######################################################################
# Sphinx documentation

sphinx_target = custom_target( 'mbh_sphinx',
                               output : 'html',
                               command : [ sphinx_exe,
                                           '-b', 'html',
                                           '-Dbreathe_projects.MBH=' +
                                           meson.build_root() +
                                           '/doc/xml',
                                           meson.current_source_dir() +
                                           '/source',
                                           'doc/sphinx/html' ],
                               install : true,
                               install_dir : man_path )

#######################################################################
