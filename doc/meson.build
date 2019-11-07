#######################################################################
# External dependencies

# Doxygen executable

doxy_exe = find_program( [ 'doxygen' ],
                         required : true )

# Sphynx executable

sphinx_exe = find_program( [ 'sphinx-quickstart' ],
                           required : true )

#######################################################################
# Doxygen documentation

man_path = '/'.join( [ get_option( 'prefix' ),
                       get_option( 'mandir' ) ] )

conf_data = configuration_data()
conf_data.set( 'DOXYGEN_OUTPUT_DIR', 'doc' )
conf_data.set( 'DOXYGEN_INPUT_DIR', root + '/mbh')

doxy_file = configure_file( output : 'doxyfile',
                            input : 'doxyfile.in',
                            configuration : conf_data,
                            install : false )

doxy_target = custom_target( 'mbh_doxy',
                             input : doxy_file,
                             output : 'html',
                             command : [ doxy_exe, doxy_file ],
                             install : true,
                             install_dir : man_path )

#######################################################################
# Sphynx documentation

# sphynx_target = custom_target( 'mbh_sphynx',
#                                input : 'conf.py',
#                                output : 'html',
#                                command : [ sphynx_exe, '-b html', sourcedir, builddir ],
#                                install : true,
#                                install_dir : man_path )

#######################################################################
