Name:           ros-noetic-moveit_fake_controller_manager
Version:        noetic.1.1.11
Release:        1%{?dist}
Summary:        ROS package moveit_fake_controller_manager

License:        BSD
URL:            http://moveit.ros.org

Source0:        https://github.com/ros-gbp/moveit-release/archive/release/noetic/moveit_fake_controller_manager/1.1.11-1.tar.gz#/ros-noetic-moveit_fake_controller_manager-1.1.11-source0.tar.gz



# common BRs
BuildRequires:  boost-devel
BuildRequires:  console-bridge-devel
BuildRequires:  gtest-devel
BuildRequires:  log4cxx-devel
BuildRequires:  python3-devel
BuildRequires:  python-unversioned-command

BuildRequires:  eigen3-devel
BuildRequires:  fcl-devel
BuildRequires:  poco-devel
BuildRequires:  tinyxml-devel
BuildRequires:  tinyxml2-devel
BuildRequires:  urdfdom-devel
BuildRequires:  ros-noetic-catkin-devel
BuildRequires:  ros-noetic-moveit_core-devel
BuildRequires:  ros-noetic-moveit_ros_planning-devel
BuildRequires:  ros-noetic-pluginlib-devel
BuildRequires:  ros-noetic-roscpp-devel

Requires:       ros-noetic-moveit_core
Requires:       ros-noetic-moveit_ros_planning
Requires:       ros-noetic-pluginlib
Requires:       ros-noetic-roscpp

Provides:  ros-noetic-moveit_fake_controller_manager = 1.1.11-1
Obsoletes: ros-noetic-moveit_fake_controller_manager < 1.1.11-1
Obsoletes: ros-kinetic-moveit_fake_controller_manager < 1.1.11-1



%description
A fake controller manager plugin for MoveIt.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ros-noetic-catkin-devel
Requires:       eigen3-devel
Requires:       fcl-devel
Requires:       poco-devel
Requires:       tinyxml-devel
Requires:       tinyxml2-devel
Requires:       urdfdom-devel
Requires:       ros-noetic-moveit_core-devel
Requires:       ros-noetic-moveit_ros_planning-devel
Requires:       ros-noetic-pluginlib-devel
Requires:       ros-noetic-roscpp-devel

Provides: ros-noetic-moveit_fake_controller_manager-devel = 1.1.11-1
Obsoletes: ros-noetic-moveit_fake_controller_manager-devel < 1.1.11-1
Obsoletes: ros-kinetic-moveit_fake_controller_manager-devel < 1.1.11-1


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

CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ; \
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS ; \
FFLAGS="${FFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}}" ; export FFLAGS ; \
FCFLAGS="${FCFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}}" ; export FCFLAGS ; \
%{?__global_ldflags:LDFLAGS="${LDFLAGS:-%__global_ldflags}" ; export LDFLAGS ;} \

source %{_libdir}/ros/setup.bash

# substitute shebang before install block because we run the local catkin script
%py3_shebang_fix .

DESTDIR=%{buildroot} ; export DESTDIR


catkin_make_isolated \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCATKIN_ENABLE_TESTING=OFF \
  -DPYTHON_VERSION=%{python3_version} \
  -DPYTHON_VERSION_NODOTS=%{python3_version_nodots} \
  --source . \
  --install \
  --install-space %{_libdir}/ros/ \
  --pkg moveit_fake_controller_manager




rm -rf %{buildroot}/%{_libdir}/ros/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh}

touch files.list
find %{buildroot}/%{_libdir}/ros/{bin,etc,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros/{include,lib*/pkgconfig,share/moveit_fake_controller_manager/cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files_devel.list

find . -maxdepth 1 -type f -iname "*readme*" | sed "s:^:%%doc :" >> files.list
find . -maxdepth 1 -type f -iname "*license*" | sed "s:^:%%license :" >> files.list



# replace cmake python macro in shebang
for file in $(grep -rIl '^#!.*@PYTHON_EXECUTABLE@.*$' %{buildroot}) ; do
  sed -i.orig 's:^#!\s*@PYTHON_EXECUTABLE@\s*:%{__python3}:' $file
  touch -r $file.orig $file
  rm $file.orig
done


echo "This is a package automatically generated with rosfed." >> README_FEDORA
echo "See https://pagure.io/ros for more information." >> README_FEDORA
install -m 0644 -p -D -t %{buildroot}/%{_docdir}/%{name} README_FEDORA
echo %{_docdir}/%{name} >> files.list
install -m 0644 -p -D -t %{buildroot}/%{_docdir}/%{name}-devel README_FEDORA
echo %{_docdir}/%{name}-devel >> files_devel.list

%py3_shebang_fix %{buildroot}

# Also fix .py.in files
for pyfile in $(grep -rIl '^#!.*python.*$' %{buildroot}) ; do
  %py3_shebang_fix $pyfile
done


%files -f files.list
%files devel -f files_devel.list


%changelog
* 2023-04-17 Ryan Wüest <ryan.wueest@protonmail.com> - noetic.1.1.11-1
- Generate moveit packages
