# Meta Package
Name:           ros-jazzy-gz-ogre-next-vendor
Version:        0.0.5
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://www.ogre3d.org/
Summary:        Meta package for ros2-jazzy-gz_ogre_next_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-gz_ogre_next_vendor
Requires:       ros2-jazzy-gz_ogre_next_vendor-devel

Obsoletes: ros-jazzy-gz-ogre-next-vendor < 0.0.5-1

%description
Vendor package for Ogre-next v2.3.3

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.5-1
- Update to latest release
