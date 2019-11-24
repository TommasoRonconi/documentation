#######################################################################
# Install python module

install_subdir( 'mbhpy', install_dir : 'python' )

#######################################################################
# Configure python module

conf_data = configuration_data()
conf_data.set( 'MBH_WRAP_PATH', mbh_c_path )

configure_file( output : 'utils.py',
                input : 'utils.py.in',
                configuration : conf_data,
                install : true,
                install_dir : 'python/mbhpy/utils' )

#######################################################################


