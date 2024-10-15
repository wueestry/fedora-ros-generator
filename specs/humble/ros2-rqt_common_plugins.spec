Name:           ros2-humble-rqt_common_plugins
Version:        1.2.0
Release:        1%{?dist}
Summary:        ROS package rqt_common_plugins

License:        BSD
URL:            http://ros.org/wiki/rqt_common_plugins

Source0:        https://github.com/ros2-gbp/rqt_common_plugins-release/archive/release/humble/rqt_common_plugins/1.2.0-1.tar.gz#/ros2-humble-rqt_common_plugins-1.2.0-source0.tar.gz


BuildArch: noarch

# common BRs
BuildRequires: patchelf
BuildRequires: coreutils
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: git
BuildRequires: make
BuildRequires: patch
BuildRequires: python3-devel
BuildRequires: python-unversioned-command
BuildRequires: python3-colcon-common-extensions
BuildRequires: python3-pip
BuildRequires: python3-pydocstyle
BuildRequires: python3-pytest
BuildRequires: python3-pytest-repeat
BuildRequires: python3-pytest-rerunfailures
BuildRequires: python3-rosdep
BuildRequires: python3-setuptools
BuildRequires: python3-vcstool

# BuildRequires:  boost-devel
# BuildRequires:  console-bridge-devel
# BuildRequires:  gtest-devel
# BuildRequires:  log4cxx-devel
# BuildRequires:  python3-devel
# BuildRequires:  python3-colcon-common-extensions
# BuildRequires:  python-unversioned-command

BuildRequires:  ros2-humble-ament_cmake-devel
BuildRequires:  ros2-humble-ament_package-devel

Requires:       ros2-humble-rqt_action
Requires:       ros2-humble-rqt_bag
Requires:       ros2-humble-rqt_bag_plugins
Requires:       ros2-humble-rqt_console
Requires:       ros2-humble-rqt_graph
Requires:       ros2-humble-rqt_image_view
Requires:       ros2-humble-rqt_msg
Requires:       ros2-humble-rqt_plot
Requires:       ros2-humble-rqt_publisher
Requires:       ros2-humble-rqt_py_common
Requires:       ros2-humble-rqt_py_console
Requires:       ros2-humble-rqt_reconfigure
Requires:       ros2-humble-rqt_service_caller
Requires:       ros2-humble-rqt_shell
Requires:       ros2-humble-rqt_srv
Requires:       ros2-humble-rqt_topic

Provides:  ros2-humble-rqt_common_plugins = 1.2.0-1
Obsoletes: ros2-humble-rqt_common_plugins < 1.2.0-1



%description
rqt_common_plugins metapackage provides ROS backend graphical tools
suite that can be used on/off of robot runtime.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ros2-humble-ament_cmake-devel
Requires:       ros2-humble-ament_package-devel
Requires:       ros2-humble-rqt_action-devel
Requires:       ros2-humble-rqt_bag-devel
Requires:       ros2-humble-rqt_bag_plugins-devel
Requires:       ros2-humble-rqt_console-devel
Requires:       ros2-humble-rqt_graph-devel
Requires:       ros2-humble-rqt_image_view-devel
Requires:       ros2-humble-rqt_msg-devel
Requires:       ros2-humble-rqt_plot-devel
Requires:       ros2-humble-rqt_publisher-devel
Requires:       ros2-humble-rqt_py_common-devel
Requires:       ros2-humble-rqt_py_console-devel
Requires:       ros2-humble-rqt_reconfigure-devel
Requires:       ros2-humble-rqt_service_caller-devel
Requires:       ros2-humble-rqt_shell-devel
Requires:       ros2-humble-rqt_srv-devel
Requires:       ros2-humble-rqt_topic-devel

Provides: ros2-humble-rqt_common_plugins-devel = 1.2.0-1
Obsoletes: ros2-humble-rqt_common_plugins-devel < 1.2.0-1


%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.



%prep

%setup -c -T
tar --strip-components=1 -xf %{SOURCE0}

%build
# nothing to do here


%install

PYTHONUNBUFFERED=1 ; export PYTHONUNBUFFERED
GZ_BUILD_FROM_SURCE=1; export GZ_BUILD_FROM_SOURCE
export GZ_VERSION=harmonic;

CFLAGS=" -Wno-error ${CFLAGS:-%optflags} -Wno-error -w -Wno-error=int-conversion" ; export CFLAGS ; \
CXXFLAGS=" -Wno-error ${CXXFLAGS:-%optflags} -Wno-error -w -Wno-error=int-conversion" ; export CXXFLAGS ; \
FFLAGS=" -Wno-error ${FFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}} -w -Wno-error=int-conversion" ; export FFLAGS ; \
FCFLAGS="${FCFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}} -w -Wno-error=int-conversion" ; export FCFLAGS ; \
%{?__global_ldflags:LDFLAGS="${LDFLAGS:-%__global_ldflags}" ; export LDFLAGS ;} \

source %{_libdir}/ros2-humble/setup.bash

# substitute shebang before install block because we run the local catkin script
%py3_shebang_fix .

# DESTDIR=%{buildroot} ; export DESTDIR

colcon \
  build \
  --merge-install \
  --cmake-args -DPYTHON_EXECUTABLE="/usr/bin/python" \
  -DTHIRDPARTY_Asio=ON \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_CXX_FLAGS="$CXXFLAGS" \
  -DCMAKE_C_FLAGS="$CFLAGS" \
  -DCMAKE_LD_FLAGS="$LDFLAGS" \
  -DBUILD_TESTING=OFF \
  -Dgz_add_get_install_prefix_impl_OVERRIDE_INSTALL_PREFIX_ENV_VARIABLE="%{_libdir}/ros2-humble/opt/" \
  --base-paths . \
  --install-base %{buildroot}/%{_libdir}/ros2-humble/ \
  --packages-select rqt_common_plugins



# remove wrong buildroot prefixes
# find %{buildroot}/%{_libdir}/ros2-humble/ -type f -exec sed -i "s:%{buildroot}::g" {} \;
# we should exclude binaries from that as it might corrupt shared libraries
find %{buildroot}/%{_libdir}/ros2-humble/ -type f ! -name '*.so*' -exec sh -c 'file "{}" | grep -q text && sed -i "s:%{buildroot}::g" "{}"' \;

# # Move include directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-humble/opt/rqt_common_plugins/include ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-humble/include/rqt_common_plugins ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-humble/include/rqt_common_plugins
#     fi
#     # Move the directory
#     cp -r %{buildroot}/%{_libdir}/ros2-humble/opt/rqt_common_plugins/include/* %{buildroot}/%{_libdir}/ros2-humble/include/rqt_common_plugins/
#     rm -rd %{buildroot}/%{_libdir}/ros2-humble/opt/rqt_common_plugins/include
# fi

# if [ -d %{buildroot}/%{_libdir}/ros2-humble/opt/rqt_common_plugins/extra_cmake ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-humble/rqt_common_plugins/extra_cmake ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-humble/rqt_common_plugins/extra_cmake
#     fi
#     # Move the directory
#     cp -r %{buildroot}/%{_libdir}/ros2-humble/opt/rqt_common_plugins/extra_cmake/* %{buildroot}/%{_libdir}/ros2-humble/rqt_common_plugins/extra_cmake/
#     rm -rd %{buildroot}/%{_libdir}/ros2-humble/opt/rqt_common_plugins/extra_cmake
# fi

# if [ -d %{buildroot}/%{_libdir}/ros2-humble/rqt_common_plugins/share ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-humble/share/rqt_common_plugins ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-humble/share/rqt_common_plugins
#     fi
#     # Move the directory
#     cp -r %{buildroot}/%{_libdir}/ros2-humble/rqt_common_plugins/share/* %{buildroot}/%{_libdir}/ros2-humble/share/rqt_common_plugins/
#     rm -rd %{buildroot}/%{_libdir}/ros2-humble/rqt_common_plugins/share
# fi

# # Move other opt path if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-humble/opt/rqt_common_plugins]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-humble ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-humble
#     fi
#     # Move the directory
#     cp -r %{buildroot}/%{_libdir}/ros2-humble/opt/rqt_common_plugins/* %{buildroot}/%{_libdir}/ros2-humble/
#     rm  -rd %{buildroot}/%{_libdir}/ros2-humble/opt/rqt_common_plugins
# fi

rm -rf %{buildroot}/%{_libdir}/ros2-humble/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh,.colcon_install_layout,COLCON_IGNORE,_local_setup*,_local_setup*}

# vendor pkg removal
rm -rf %{buildroot}/%{_libdir}/ros2-humble/opt/share/rqt_common_plugins/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh,.colcon_install_layout,COLCON_IGNORE,_local_setup*,_local_setup*}

# remove __pycache__
find %{buildroot} -type d -name '__pycache__' -exec rm -rf {} +
find . -name '*.pyc' -delete

touch files.list
find %{buildroot}/%{_libdir}/ros2-humble/{share,bin,etc,tools,lib64/python*,lib/python*/site-packages} \
  ! -name cmake ! -name include \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros2-humble/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

# paths for vendor packages
find %{buildroot}/%{_libdir}/ros2-humble/rqt_common_plugins/{bin,etc,tools,lib64/python*,lib/python*/site-packages,share} \
  ! -name cmake ! -name include \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files.list
find %{buildroot}/%{_libdir}/ros2-humble/opt/rqt_common_plugins/{bin,etc,tools,lib64/python*,lib/python*/site-packages,share} \
  ! -name cmake ! -name include \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files.list
find %{buildroot}/%{_libdir}/ros2-humble/rqt_common_plugins/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list
find %{buildroot}/%{_libdir}/ros2-humble/opt/rqt_common_plugins/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list
find %{buildroot}/%{_libdir}/ros2-humble/opt/share/rqt_common_plugins \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros2-humble/{lib*/pkgconfig,include/,cmake/,rqt_common_plugins/include/,share/rqt_common_plugins/cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files_devel.list
# paths for vendor packages
find %{buildroot}/%{_libdir}/ros2-humble/rqt_common_plugins/{lib*/pkgconfig,include/,cmake/,rqt_common_plugins/include/,share/cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-humble/opt/rqt_common_plugins/extra_cmake \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-humble/opt/rqt_common_plugins/{lib*/pkgconfig,include/,cmake/,rqt_common_plugins/include/,/share/cmake,/extra_cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-humble/opt/share/ament_index/resource_index \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-humble/opt/share/colcon-core/packages/ \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-humble/opt/share/rqt_common_plugins/{hook,environment,cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find . -maxdepth 1 -type f -iname "*license*" | sed "s:^:%%license :" >> files.list



find %{buildroot}/%{_libdir}/ros2-humble/ -name *__rosidl_generator_py.so -type f -exec patchelf --remove-rpath  {} \;
# find %{buildroot}/%{_libdir}/ros2-humble/ -name *__rosidl_generator_py.so -type f -exec patchelf --force-rpath --add-rpath "%{_libdir}/ros2/lib" {} \;
find %{buildroot}/%{_libdir}/ros2-humble/ -name "*.so*" -type f -exec patchelf  --shrink-rpath --allowed-rpath-prefixes %{_libdir} {} \;

# replace cmake python macro in shebang
for file in $(grep -rIl '^#!.*@PYTHON_EXECUTABLE@.*$' %{buildroot}) ; do
  sed -i.orig 's:^#!\s*@PYTHON_EXECUTABLE@\s*:%{__python3}:' $file
  touch -r $file.orig $file
  rm $file.orig
done


echo "This is a package automatically generated with rosfed." >> README_FEDORA
echo "See  https://github.com/TarikViehmann/rosfed for more information." >> README_FEDORA
install -m 0644 -p -D -t %{buildroot}/%{_docdir}/%{name} README_FEDORA
echo %{_docdir}/%{name} >> files.list
install -m 0644 -p -D -t %{buildroot}/%{_docdir}/%{name}-devel README_FEDORA
echo %{_docdir}/%{name}-devel >> files_devel.list

%py3_shebang_fix %{buildroot}

# Also fix .py.in files
for pyfile in $(grep -rIl '^#!.*python.*$' %{buildroot}) ; do
  %py3_shebang_fix $pyfile
done

sort files.list | uniq > files.list.tmp && mv files.list.tmp files.list
sort files_devel.list | uniq > files_devel.list.tmp && mv files_devel.list.tmp files_devel.list

%files -f files.list
%files devel -f files_devel.list


%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.2.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.2.0-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.2.0-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.0.4.9-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.2.0-1
- Initial humble build
