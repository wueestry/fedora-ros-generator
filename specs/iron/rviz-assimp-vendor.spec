# Meta Package
Name:           ros-iron-rviz-assimp-vendor
Version:        12.4.7
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://assimp.sourceforge.net/index.html
Summary:        Meta package for ros2-iron-rviz_assimp_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rviz_assimp_vendor
Requires:       ros2-iron-rviz_assimp_vendor-devel

Obsoletes: ros-iron-rviz-assimp-vendor < 12.4.7-1

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
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.12.4.7-1
- Update to latest release
