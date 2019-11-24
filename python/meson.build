#######################################################################
# Install python module

install_subdir( 'mbhpy', install_dir : 'python' )

#######################################################################
# Configure python module

conf_data = configuration_data()

configure_file( output : 'utils.py',
                input : 'utils.py.in',
                configuration : conf_data,
                install : true,
                install_dir : 'python/mbhpy/utils' )

#######################################################################


