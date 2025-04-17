Name:           ros2-jazzy-nav2_smac_planner
Version:        1.3.5
Release:        1%{?dist}
Summary:        ROS package nav2_smac_planner

License:        Apache-2.0
URL:            http://www.ros.org/

Source0:        https://github.com/SteveMacenski/navigation2-release/archive/release/jazzy/nav2_smac_planner/1.3.5-1.tar.gz#/ros2-jazzy-nav2_smac_planner-1.3.5-source0.tar.gz



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

BuildRequires:  eigen3-devel
BuildRequires:  json-devel
BuildRequires:  ros2-jazzy-ament_cmake-devel
BuildRequires:  ros2-jazzy-ament_package-devel
BuildRequires:  ros2-jazzy-angles-devel
BuildRequires:  ros2-jazzy-builtin_interfaces-devel
BuildRequires:  ros2-jazzy-eigen3_cmake_module-devel
BuildRequires:  ros2-jazzy-geometry_msgs-devel
BuildRequires:  ros2-jazzy-nav2_common-devel
BuildRequires:  ros2-jazzy-nav2_core-devel
BuildRequires:  ros2-jazzy-nav2_costmap_2d-devel
BuildRequires:  ros2-jazzy-nav2_msgs-devel
BuildRequires:  ros2-jazzy-nav2_util-devel
BuildRequires:  ros2-jazzy-nav_msgs-devel
BuildRequires:  ros2-jazzy-ompl-devel
BuildRequires:  ros2-jazzy-pluginlib-devel
BuildRequires:  ros2-jazzy-rclcpp-devel
BuildRequires:  ros2-jazzy-rclcpp_action-devel
BuildRequires:  ros2-jazzy-rclcpp_lifecycle-devel
BuildRequires:  ros2-jazzy-tf2_ros-devel
BuildRequires:  ros2-jazzy-visualization_msgs-devel

Requires:       ros2-jazzy-angles
Requires:       ros2-jazzy-builtin_interfaces
Requires:       ros2-jazzy-eigen3_cmake_module
Requires:       ros2-jazzy-geometry_msgs
Requires:       ros2-jazzy-nav2_common
Requires:       ros2-jazzy-nav2_core
Requires:       ros2-jazzy-nav2_costmap_2d
Requires:       ros2-jazzy-nav2_msgs
Requires:       ros2-jazzy-nav2_util
Requires:       ros2-jazzy-nav_msgs
Requires:       ros2-jazzy-ompl
Requires:       ros2-jazzy-pluginlib
Requires:       ros2-jazzy-rclcpp
Requires:       ros2-jazzy-rclcpp_action
Requires:       ros2-jazzy-rclcpp_lifecycle
Requires:       ros2-jazzy-tf2_ros
Requires:       ros2-jazzy-visualization_msgs

Provides:  ros2-jazzy-nav2_smac_planner = 1.3.5-1
Obsoletes: ros2-jazzy-nav2_smac_planner < 1.3.5-1



%description
Smac global planning plugin: A*, Hybrid-A*, State Lattice

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ros2-jazzy-ament_cmake-devel
Requires:       eigen3-devel
Requires:       json-devel
Requires:       ros2-jazzy-ament_package-devel
Requires:       ros2-jazzy-angles-devel
Requires:       ros2-jazzy-builtin_interfaces-devel
Requires:       ros2-jazzy-eigen3_cmake_module-devel
Requires:       ros2-jazzy-geometry_msgs-devel
Requires:       ros2-jazzy-nav2_common-devel
Requires:       ros2-jazzy-nav2_core-devel
Requires:       ros2-jazzy-nav2_costmap_2d-devel
Requires:       ros2-jazzy-nav2_msgs-devel
Requires:       ros2-jazzy-nav2_util-devel
Requires:       ros2-jazzy-nav_msgs-devel
Requires:       ros2-jazzy-ompl-devel
Requires:       ros2-jazzy-pluginlib-devel
Requires:       ros2-jazzy-rclcpp-devel
Requires:       ros2-jazzy-rclcpp_action-devel
Requires:       ros2-jazzy-rclcpp_lifecycle-devel
Requires:       ros2-jazzy-tf2_ros-devel
Requires:       ros2-jazzy-visualization_msgs-devel

Provides: ros2-jazzy-nav2_smac_planner-devel = 1.3.5-1
Obsoletes: ros2-jazzy-nav2_smac_planner-devel < 1.3.5-1


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

source %{_libdir}/ros2-jazzy/setup.bash

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
  -Dgz_add_get_install_prefix_impl_OVERRIDE_INSTALL_PREFIX_ENV_VARIABLE="%{_libdir}/ros2-jazzy/opt/" \
  --base-paths . \
  --install-base %{buildroot}/%{_libdir}/ros2-jazzy/ \
  --packages-select nav2_smac_planner



# remove wrong buildroot prefixes
# find %{buildroot}/%{_libdir}/ros2-jazzy/ -type f -exec sed -i "s:%{buildroot}::g" {} \;
# we should exclude binaries from that as it might corrupt shared libraries
find %{buildroot}/%{_libdir}/ros2-jazzy/ -type f ! -name '*.so*' -exec sh -c 'file "{}" | grep -q text && sed -i "s:%{buildroot}::g" "{}"' \;

# # Move include directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-jazzy/opt/nav2_smac_planner/include ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-jazzy/include/nav2_smac_planner ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-jazzy/include/nav2_smac_planner
#     fi
#     # Move the directory
#     cp -r %{buildroot}/%{_libdir}/ros2-jazzy/opt/nav2_smac_planner/include/* %{buildroot}/%{_libdir}/ros2-jazzy/include/nav2_smac_planner/
#     rm -rd %{buildroot}/%{_libdir}/ros2-jazzy/opt/nav2_smac_planner/include
# fi

# if [ -d %{buildroot}/%{_libdir}/ros2-jazzy/opt/nav2_smac_planner/extra_cmake ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-jazzy/nav2_smac_planner/extra_cmake ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-jazzy/nav2_smac_planner/extra_cmake
#     fi
#     # Move the directory
#     cp -r %{buildroot}/%{_libdir}/ros2-jazzy/opt/nav2_smac_planner/extra_cmake/* %{buildroot}/%{_libdir}/ros2-jazzy/nav2_smac_planner/extra_cmake/
#     rm -rd %{buildroot}/%{_libdir}/ros2-jazzy/opt/nav2_smac_planner/extra_cmake
# fi

# if [ -d %{buildroot}/%{_libdir}/ros2-jazzy/nav2_smac_planner/share ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-jazzy/share/nav2_smac_planner ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-jazzy/share/nav2_smac_planner
#     fi
#     # Move the directory
#     cp -r %{buildroot}/%{_libdir}/ros2-jazzy/nav2_smac_planner/share/* %{buildroot}/%{_libdir}/ros2-jazzy/share/nav2_smac_planner/
#     rm -rd %{buildroot}/%{_libdir}/ros2-jazzy/nav2_smac_planner/share
# fi

# # Move other opt path if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-jazzy/opt/nav2_smac_planner]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-jazzy ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-jazzy
#     fi
#     # Move the directory
#     cp -r %{buildroot}/%{_libdir}/ros2-jazzy/opt/nav2_smac_planner/* %{buildroot}/%{_libdir}/ros2-jazzy/
#     rm  -rd %{buildroot}/%{_libdir}/ros2-jazzy/opt/nav2_smac_planner
# fi

rm -rf %{buildroot}/%{_libdir}/ros2-jazzy/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh,.colcon_install_layout,COLCON_IGNORE,_local_setup*,_local_setup*}

# vendor pkg removal
rm -rf %{buildroot}/%{_libdir}/ros2-jazzy/opt/share/nav2_smac_planner/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh,.colcon_install_layout,COLCON_IGNORE,_local_setup*,_local_setup*}

# remove __pycache__
find %{buildroot} -type d -name '__pycache__' -exec rm -rf {} +
find . -name '*.pyc' -delete

touch files.list
find %{buildroot}/%{_libdir}/ros2-jazzy/{share,bin,etc,tools,lib64/python*,lib/python*/site-packages,lib/python*/dist-packages} \
  ! -name cmake ! -name include \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros2-jazzy/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

# paths for vendor packages
find %{buildroot}/%{_libdir}/ros2-jazzy/nav2_smac_planner/{bin,etc,tools,lib64/python*,lib/python*/site-packages,share} \
  ! -name cmake ! -name include \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/nav2_smac_planner/{bin,etc,tools,lib64/python*,lib/python*/site-packages,share} \
  ! -name cmake ! -name include \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files.list
find %{buildroot}/%{_libdir}/ros2-jazzy/nav2_smac_planner/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/nav2_smac_planner/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/share/nav2_smac_planner \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros2-jazzy/{lib*/pkgconfig,include/,cmake/,nav2_smac_planner/include/,share/nav2_smac_planner/cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files_devel.list
# paths for vendor packages
find %{buildroot}/%{_libdir}/ros2-jazzy/nav2_smac_planner/{lib*/pkgconfig,include/,cmake/,extra_cmake/,nav2_smac_planner/include/,share/cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/nav2_smac_planner/extra_cmake \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/nav2_smac_planner/{lib*/pkgconfig,include/,cmake/,nav2_smac_planner/include/,/share/cmake,/extra_cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/share/ament_index/resource_index \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/share/colcon-core/packages/ \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/share/nav2_smac_planner/{hook,environment,cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find . -maxdepth 1 -type f -iname "*license*" | sed "s:^:%%license :" >> files.list



find %{buildroot}/%{_libdir}/ros2-jazzy/ -name *__rosidl_generator_py.so -type f -exec patchelf --remove-rpath  {} \;
# find %{buildroot}/%{_libdir}/ros2-jazzy/ -name *__rosidl_generator_py.so -type f -exec patchelf --force-rpath --add-rpath "%{_libdir}/ros2/lib" {} \;
find %{buildroot}/%{_libdir}/ros2-jazzy/ -name "*.so*" -type f -exec patchelf  --shrink-rpath --allowed-rpath-prefixes %{_libdir} {} \;

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
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.5-1
- Update to latest release
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.4-1
- Update to latest release
* Wed Nov 20 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.3-1
- Update to latest release
* Mon Aug 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.2-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.1-1
- Update to latest release
