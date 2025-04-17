# Meta Package
Name:           ros-jazzy-rviz-ogre-vendor
Version:        14.1.8
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://www.ogre3d.org/
Summary:        Meta package for ros2-jazzy-rviz_ogre_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rviz_ogre_vendor
Requires:       ros2-jazzy-rviz_ogre_vendor-devel

Obsoletes: ros-jazzy-rviz-ogre-vendor < 14.1.8-1

%description
Wrapper around ogre3d, it provides a fixed CMake module and an
ExternalProject build of ogre.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 05 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.14.1.8-1
- Update to latest release
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.14.1.7-1
- Update to latest release
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.14.1.6-1
- Update to latest release
* Tue Oct 15 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.14.1.5-1
- Update to latest release
* Mon Aug 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.14.1.4-1
- Update to latest release
* Wed Jul 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.14.1.3-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.14.1.2-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.14.1.1-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.14.1.0-1
- Update to latest release
