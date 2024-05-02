# Meta Package
Name:           ros-jazzy-rviz-assimp-vendor
Version:        14.1.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://assimp.sourceforge.net/index.html
Summary:        Meta package for ros2-jazzy-rviz_assimp_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rviz_assimp_vendor
Requires:       ros2-jazzy-rviz_assimp_vendor-devel

Obsoletes: ros-jazzy-rviz-assimp-vendor < 14.1.0-1

%description
Wrapper around assimp, providing nothing but a dependency on assimp,
on some systems. On others, it provides a fixed CMake module or even
an ExternalProject build of assimp.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.14.1.0-1
- Update to latest release
