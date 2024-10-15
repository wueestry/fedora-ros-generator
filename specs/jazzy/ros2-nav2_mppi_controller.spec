Name:           ros2-jazzy-nav2_mppi_controller
Version:        1.3.2
Release:        1%{?dist}
Summary:        ROS package nav2_mppi_controller

License:        MIT
URL:            http://www.ros.org/

Source0:        https://github.com/SteveMacenski/navigation2-release/archive/release/jazzy/nav2_mppi_controller/1.3.2-1.tar.gz#/ros2-jazzy-nav2_mppi_controller-1.3.2-source0.tar.gz

Patch0: ros2-nav2_mppi_controller.disable-warnings.patch


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

BuildRequires:  google-benchmark-devel
BuildRequires:  libomp-devel
BuildRequires:  xsimd-devel
BuildRequires:  xtensor-devel
BuildRequires:  ros2-jazzy-ament_cmake-devel
BuildRequires:  ros2-jazzy-ament_cmake_ros-devel
BuildRequires:  ros2-jazzy-ament_package-devel
BuildRequires:  ros2-jazzy-geometry_msgs-devel
BuildRequires:  ros2-jazzy-nav2_common-devel
BuildRequires:  ros2-jazzy-nav2_core-devel
BuildRequires:  ros2-jazzy-nav2_costmap_2d-devel
BuildRequires:  ros2-jazzy-nav2_msgs-devel
BuildRequires:  ros2-jazzy-nav2_util-devel
BuildRequires:  ros2-jazzy-pluginlib-devel
BuildRequires:  ros2-jazzy-rclcpp-devel
BuildRequires:  ros2-jazzy-std_msgs-devel
BuildRequires:  ros2-jazzy-tf2-devel
BuildRequires:  ros2-jazzy-tf2_eigen-devel
BuildRequires:  ros2-jazzy-tf2_geometry_msgs-devel
BuildRequires:  ros2-jazzy-tf2_ros-devel
BuildRequires:  ros2-jazzy-visualization_msgs-devel

Requires:       ros2-jazzy-geometry_msgs
Requires:       ros2-jazzy-nav2_common
Requires:       ros2-jazzy-nav2_core
Requires:       ros2-jazzy-nav2_costmap_2d
Requires:       ros2-jazzy-nav2_msgs
Requires:       ros2-jazzy-nav2_util
Requires:       ros2-jazzy-pluginlib
Requires:       ros2-jazzy-rclcpp
Requires:       ros2-jazzy-std_msgs
Requires:       ros2-jazzy-tf2
Requires:       ros2-jazzy-tf2_eigen
Requires:       ros2-jazzy-tf2_geometry_msgs
Requires:       ros2-jazzy-tf2_ros
Requires:       ros2-jazzy-visualization_msgs

Provides:  ros2-jazzy-nav2_mppi_controller = 1.3.2-1
Obsoletes: ros2-jazzy-nav2_mppi_controller < 1.3.2-1



%description
nav2_mppi_controller

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ros2-jazzy-ament_cmake-devel
Requires:       ros2-jazzy-ament_cmake_ros-devel
Requires:       google-benchmark-devel
Requires:       libomp-devel
Requires:       xsimd-devel
Requires:       xtensor-devel
Requires:       ros2-jazzy-ament_package-devel
Requires:       ros2-jazzy-geometry_msgs-devel
Requires:       ros2-jazzy-nav2_common-devel
Requires:       ros2-jazzy-nav2_core-devel
Requires:       ros2-jazzy-nav2_costmap_2d-devel
Requires:       ros2-jazzy-nav2_msgs-devel
Requires:       ros2-jazzy-nav2_util-devel
Requires:       ros2-jazzy-pluginlib-devel
Requires:       ros2-jazzy-rclcpp-devel
Requires:       ros2-jazzy-std_msgs-devel
Requires:       ros2-jazzy-tf2-devel
Requires:       ros2-jazzy-tf2_eigen-devel
Requires:       ros2-jazzy-tf2_geometry_msgs-devel
Requires:       ros2-jazzy-tf2_ros-devel
Requires:       ros2-jazzy-visualization_msgs-devel

Provides: ros2-jazzy-nav2_mppi_controller-devel = 1.3.2-1
Obsoletes: ros2-jazzy-nav2_mppi_controller-devel < 1.3.2-1


%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.



%prep

%setup -c -T
tar --strip-components=1 -xf %{SOURCE0}
%patch 0 -p1

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
  --packages-select nav2_mppi_controller



# remove wrong buildroot prefixes
# find %{buildroot}/%{_libdir}/ros2-jazzy/ -type f -exec sed -i "s:%{buildroot}::g" {} \;
# we should exclude binaries from that as it might corrupt shared libraries
find %{buildroot}/%{_libdir}/ros2-jazzy/ -type f ! -name '*.so*' -exec sh -c 'file "{}" | grep -q text && sed -i "s:%{buildroot}::g" "{}"' \;

# # Move include directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-jazzy/opt/nav2_mppi_controller/include ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-jazzy/include/nav2_mppi_controller ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-jazzy/include/nav2_mppi_controller
#     fi
#     # Move the directory
#     cp -r %{buildroot}/%{_libdir}/ros2-jazzy/opt/nav2_mppi_controller/include/* %{buildroot}/%{_libdir}/ros2-jazzy/include/nav2_mppi_controller/
#     rm -rd %{buildroot}/%{_libdir}/ros2-jazzy/opt/nav2_mppi_controller/include
# fi

# if [ -d %{buildroot}/%{_libdir}/ros2-jazzy/opt/nav2_mppi_controller/extra_cmake ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-jazzy/nav2_mppi_controller/extra_cmake ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-jazzy/nav2_mppi_controller/extra_cmake
#     fi
#     # Move the directory
#     cp -r %{buildroot}/%{_libdir}/ros2-jazzy/opt/nav2_mppi_controller/extra_cmake/* %{buildroot}/%{_libdir}/ros2-jazzy/nav2_mppi_controller/extra_cmake/
#     rm -rd %{buildroot}/%{_libdir}/ros2-jazzy/opt/nav2_mppi_controller/extra_cmake
# fi

# if [ -d %{buildroot}/%{_libdir}/ros2-jazzy/nav2_mppi_controller/share ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-jazzy/share/nav2_mppi_controller ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-jazzy/share/nav2_mppi_controller
#     fi
#     # Move the directory
#     cp -r %{buildroot}/%{_libdir}/ros2-jazzy/nav2_mppi_controller/share/* %{buildroot}/%{_libdir}/ros2-jazzy/share/nav2_mppi_controller/
#     rm -rd %{buildroot}/%{_libdir}/ros2-jazzy/nav2_mppi_controller/share
# fi

# # Move other opt path if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-jazzy/opt/nav2_mppi_controller]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-jazzy ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-jazzy
#     fi
#     # Move the directory
#     cp -r %{buildroot}/%{_libdir}/ros2-jazzy/opt/nav2_mppi_controller/* %{buildroot}/%{_libdir}/ros2-jazzy/
#     rm  -rd %{buildroot}/%{_libdir}/ros2-jazzy/opt/nav2_mppi_controller
# fi

rm -rf %{buildroot}/%{_libdir}/ros2-jazzy/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh,.colcon_install_layout,COLCON_IGNORE,_local_setup*,_local_setup*}

# vendor pkg removal
rm -rf %{buildroot}/%{_libdir}/ros2-jazzy/opt/share/nav2_mppi_controller/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh,.colcon_install_layout,COLCON_IGNORE,_local_setup*,_local_setup*}

# remove __pycache__
find %{buildroot} -type d -name '__pycache__' -exec rm -rf {} +
find . -name '*.pyc' -delete

touch files.list
find %{buildroot}/%{_libdir}/ros2-jazzy/{share,bin,etc,tools,lib64/python*,lib/python*/site-packages} \
  ! -name cmake ! -name include \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros2-jazzy/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

# paths for vendor packages
find %{buildroot}/%{_libdir}/ros2-jazzy/nav2_mppi_controller/{bin,etc,tools,lib64/python*,lib/python*/site-packages,share} \
  ! -name cmake ! -name include \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/nav2_mppi_controller/{bin,etc,tools,lib64/python*,lib/python*/site-packages,share} \
  ! -name cmake ! -name include \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files.list
find %{buildroot}/%{_libdir}/ros2-jazzy/nav2_mppi_controller/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/nav2_mppi_controller/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/share/nav2_mppi_controller \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros2-jazzy/{lib*/pkgconfig,include/,cmake/,nav2_mppi_controller/include/,share/nav2_mppi_controller/cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files_devel.list
# paths for vendor packages
find %{buildroot}/%{_libdir}/ros2-jazzy/nav2_mppi_controller/{lib*/pkgconfig,include/,cmake/,nav2_mppi_controller/include/,share/cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/nav2_mppi_controller/extra_cmake \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/nav2_mppi_controller/{lib*/pkgconfig,include/,cmake/,nav2_mppi_controller/include/,/share/cmake,/extra_cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/share/ament_index/resource_index \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/share/colcon-core/packages/ \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-jazzy/opt/share/nav2_mppi_controller/{hook,environment,cmake} \
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
* Mon Aug 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.2-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.1-1
- Update to latest release
