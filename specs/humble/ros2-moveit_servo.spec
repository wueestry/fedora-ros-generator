Name:           ros2-humble-moveit_servo
Version:        2.5.5
Release:        1%{?dist}
Summary:        ROS package moveit_servo

License:        BSD 3-Clause
URL:            https://ros-planning.github.io/moveit_tutorials

Source0:        https://github.com/ros2-gbp/moveit2-release/archive/release/humble/moveit_servo/2.5.5-1.tar.gz#/ros2-humble-moveit_servo-2.5.5-source0.tar.gz



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
BuildRequires:  ros2-humble-control_msgs-devel
BuildRequires:  ros2-humble-control_toolbox-devel
BuildRequires:  ros2-humble-geometry_msgs-devel
BuildRequires:  ros2-humble-moveit_common-devel
BuildRequires:  ros2-humble-moveit_core-devel
BuildRequires:  ros2-humble-moveit_msgs-devel
BuildRequires:  ros2-humble-moveit_ros_planning_interface-devel
BuildRequires:  ros2-humble-pluginlib-devel
BuildRequires:  ros2-humble-sensor_msgs-devel
BuildRequires:  ros2-humble-std_msgs-devel
BuildRequires:  ros2-humble-std_srvs-devel
BuildRequires:  ros2-humble-tf2_eigen-devel
BuildRequires:  ros2-humble-trajectory_msgs-devel

Requires:       ros2-humble-control_msgs
Requires:       ros2-humble-control_toolbox
Requires:       ros2-humble-geometry_msgs
Requires:       ros2-humble-gripper_controllers
Requires:       ros2-humble-joint_state_broadcaster
Requires:       ros2-humble-joint_trajectory_controller
Requires:       ros2-humble-joy
Requires:       ros2-humble-launch_param_builder
Requires:       ros2-humble-moveit_common
Requires:       ros2-humble-moveit_configs_utils
Requires:       ros2-humble-moveit_core
Requires:       ros2-humble-moveit_msgs
Requires:       ros2-humble-moveit_ros_planning_interface
Requires:       ros2-humble-pluginlib
Requires:       ros2-humble-robot_state_publisher
Requires:       ros2-humble-sensor_msgs
Requires:       ros2-humble-std_msgs
Requires:       ros2-humble-std_srvs
Requires:       ros2-humble-tf2_eigen
Requires:       ros2-humble-tf2_ros
Requires:       ros2-humble-trajectory_msgs

Provides:  ros2-humble-moveit_servo = 2.5.5-1
Obsoletes: ros2-humble-moveit_servo < 2.5.5-1



%description
Provides real-time manipulator Cartesian and joint servoing.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ros2-humble-ament_cmake-devel
Requires:       ros2-humble-ament_package-devel
Requires:       ros2-humble-control_msgs-devel
Requires:       ros2-humble-control_toolbox-devel
Requires:       ros2-humble-geometry_msgs-devel
Requires:       ros2-humble-moveit_common-devel
Requires:       ros2-humble-moveit_core-devel
Requires:       ros2-humble-moveit_msgs-devel
Requires:       ros2-humble-moveit_ros_planning_interface-devel
Requires:       ros2-humble-pluginlib-devel
Requires:       ros2-humble-sensor_msgs-devel
Requires:       ros2-humble-std_msgs-devel
Requires:       ros2-humble-std_srvs-devel
Requires:       ros2-humble-tf2_eigen-devel
Requires:       ros2-humble-trajectory_msgs-devel
Requires:       ros2-humble-gripper_controllers-devel
Requires:       ros2-humble-joint_state_broadcaster-devel
Requires:       ros2-humble-joint_trajectory_controller-devel
Requires:       ros2-humble-joy-devel
Requires:       ros2-humble-launch_param_builder-devel
Requires:       ros2-humble-moveit_configs_utils-devel
Requires:       ros2-humble-robot_state_publisher-devel
Requires:       ros2-humble-tf2_ros-devel

Provides: ros2-humble-moveit_servo-devel = 2.5.5-1
Obsoletes: ros2-humble-moveit_servo-devel < 2.5.5-1


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
  --packages-select moveit_servo



# remove wrong buildroot prefixes
# find %{buildroot}/%{_libdir}/ros2-humble/ -type f -exec sed -i "s:%{buildroot}::g" {} \;
# we should exclude binaries from that as it might corrupt shared libraries
find %{buildroot}/%{_libdir}/ros2-humble/ -type f ! -name '*.so*' -exec sh -c 'file "{}" | grep -q text && sed -i "s:%{buildroot}::g" "{}"' \;

# # Move include directory if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-humble/opt/moveit_servo/include ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-humble/include/moveit_servo ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-humble/include/moveit_servo
#     fi
#     # Move the directory
#     cp -r %{buildroot}/%{_libdir}/ros2-humble/opt/moveit_servo/include/* %{buildroot}/%{_libdir}/ros2-humble/include/moveit_servo/
#     rm -rd %{buildroot}/%{_libdir}/ros2-humble/opt/moveit_servo/include
# fi

# if [ -d %{buildroot}/%{_libdir}/ros2-humble/opt/moveit_servo/extra_cmake ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-humble/moveit_servo/extra_cmake ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-humble/moveit_servo/extra_cmake
#     fi
#     # Move the directory
#     cp -r %{buildroot}/%{_libdir}/ros2-humble/opt/moveit_servo/extra_cmake/* %{buildroot}/%{_libdir}/ros2-humble/moveit_servo/extra_cmake/
#     rm -rd %{buildroot}/%{_libdir}/ros2-humble/opt/moveit_servo/extra_cmake
# fi

# if [ -d %{buildroot}/%{_libdir}/ros2-humble/moveit_servo/share ]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-humble/share/moveit_servo ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-humble/share/moveit_servo
#     fi
#     # Move the directory
#     cp -r %{buildroot}/%{_libdir}/ros2-humble/moveit_servo/share/* %{buildroot}/%{_libdir}/ros2-humble/share/moveit_servo/
#     rm -rd %{buildroot}/%{_libdir}/ros2-humble/moveit_servo/share
# fi

# # Move other opt path if source path exists
# if [ -d %{buildroot}/%{_libdir}/ros2-humble/opt/moveit_servo]; then
#     # If destination path does not exist, create it
#     if [ ! -d %{buildroot}/%{_libdir}/ros2-humble ]; then
#         mkdir -p %{buildroot}/%{_libdir}/ros2-humble
#     fi
#     # Move the directory
#     cp -r %{buildroot}/%{_libdir}/ros2-humble/opt/moveit_servo/* %{buildroot}/%{_libdir}/ros2-humble/
#     rm  -rd %{buildroot}/%{_libdir}/ros2-humble/opt/moveit_servo
# fi

rm -rf %{buildroot}/%{_libdir}/ros2-humble/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh,.colcon_install_layout,COLCON_IGNORE,_local_setup*,_local_setup*}

# vendor pkg removal
rm -rf %{buildroot}/%{_libdir}/ros2-humble/opt/share/moveit_servo/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh,.colcon_install_layout,COLCON_IGNORE,_local_setup*,_local_setup*}

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
find %{buildroot}/%{_libdir}/ros2-humble/moveit_servo/{bin,etc,tools,lib64/python*,lib/python*/site-packages,share} \
  ! -name cmake ! -name include \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files.list
find %{buildroot}/%{_libdir}/ros2-humble/opt/moveit_servo/{bin,etc,tools,lib64/python*,lib/python*/site-packages,share} \
  ! -name cmake ! -name include \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files.list
find %{buildroot}/%{_libdir}/ros2-humble/moveit_servo/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list
find %{buildroot}/%{_libdir}/ros2-humble/opt/moveit_servo/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list
find %{buildroot}/%{_libdir}/ros2-humble/opt/share/moveit_servo \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros2-humble/{lib*/pkgconfig,include/,cmake/,moveit_servo/include/,share/moveit_servo/cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files_devel.list
# paths for vendor packages
find %{buildroot}/%{_libdir}/ros2-humble/moveit_servo/{lib*/pkgconfig,include/,cmake/,moveit_servo/include/,share/cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-humble/opt/moveit_servo/extra_cmake \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-humble/opt/moveit_servo/{lib*/pkgconfig,include/,cmake/,moveit_servo/include/,/share/cmake,/extra_cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-humble/opt/share/ament_index/resource_index \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-humble/opt/share/colcon-core/packages/ \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" >> files_devel.list
find %{buildroot}/%{_libdir}/ros2-humble/opt/share/moveit_servo/{hook,environment,cmake} \
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
* Wed Mar 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.5.5-1
- update to latest release
